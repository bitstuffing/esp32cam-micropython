#!/bin/bash

## This script will install and compile the requirements for ESP32-CAM to get
## a working firmware of the lastest micropython framwork in this board 
## Author @bitstuffing , in development, showing the work with love

force=false
deploy=false
help=false
generic=false

options=$@
arguments=($options)

for argument in $options
do
    case $argument in
        --force) 
            echo "Forcing install dependencies"
            force=true
        ;;
        --deploy) 
            echo "Deploy firmware"
            deploy=true
        ;;
        --generic) 
            echo "Generic firmware"
            generic=true
        ;;
        --help)
            help=true
        ;;
    esac
done

showHelp(){
       # Display Help
        echo "This script will install and compile the requirements for ESP32-CAM to get"
        echo "a working firmware of the lastest micropython framwork in this board."
        echo "Author @bitstuffing."
        echo ""
        echo ""
        echo "Syntax: ./arch-compile.sh [--force|--deploy|--help]"
        echo ""
        echo "--force   Force try to install system (compiler) dependencies (is necessary sudo permissions, it will required to)"
        echo "--generic Compile last micropython just for ESP32 (without CAM driver)"
        echo "--deploy  Deploy compiled firmware"
        echo "--help    Show this message"
        echo
}

installRequirements(){
    #first step is extracted from https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/linux-macos-setup.html
    sudo pacman -S --needed gcc git make flex bison gperf python cmake ninja ccache dfu-util libusb --noconfirm
}

installEspIdf(){
    mkdir ~/esp/
    cd ~/esp/

    #BOARD=GENERIC works with '-b release/v4.4', testing v4.4.2 specifically with ESP32_CAM
    git clone -b 'v4.4.2' --recursive https://github.com/espressif/esp-idf.git
    cd esp-idf
    #git submodule update --init --recursive

    patchXtensa

    cd ~/esp/esp-idf/
    ./install.sh
    . ./export.sh
}

patchXtensa() {
    #patch /components/xtensa/include/xtensa-debug-module.h -> add #define XCHAL_NUM_PERF_COUNTERS 2
    git checkout components/xtensa/include/xtensa-debug-module.h
    sed -i '1i #define XCHAL_NUM_PERF_COUNTERS 2' components/xtensa/include/xtensa-debug-module.h
}

deployESP32Cam() {
    #all next steps are extracted from https://github.com/lemariva/micropython-camera-driver

    cd ~/esp/esp-idf/components
    git clone https://github.com/espressif/esp32-camera.git

    cd ~/esp/
    git clone https://github.com/lemariva/micropython-camera-driver.git
}

deployAndCompileMicroPython() {
    deployMicropython
    if $generic; then
        echo "compiling GENERIC"
        compileMicroPythonESP32
    else
        echo "compiling ESP32-CAM"
        patchMicropythonESP32CAM
        compileMicroPythonESP32CAM
    fi
}

compileMicroPythonESP32() {
    cd ~/esp/micropython/ports/esp32
    #some issues related to xtensa binaries, force this information to idf.py with system environment variable
    export IDF_MAINTAINER=v4.4.2 
    make USER_C_MODULES=$HOME/esp/micropython-camera-driver/src/micropython.cmake BOARD=GENERIC all
}

compileMicroPythonESP32CAM() {
    cd ~/esp/micropython/ports/esp32
    #some issues related to xtensa binaries, force this information to idf.py with system environment variable
    export IDF_MAINTAINER=v4.4.2 
    make USER_C_MODULES=$HOME/esp/micropython-camera-driver/src/micropython.cmake BOARD=ESP32_CAM all
}

deployMicropython() {
    mkdir ~/esp/micropython
    cd ~/esp/micropython
    git clone --recursive https://github.com/micropython/micropython.git .
}

patchMicropythonESP32CAM() {
    #patch micropython with the driver requirements
    #ln -s $HOME/esp/micropython-camera-driver/boards/ESP32_CAM $HOME/esp/micropython/ports/esp32/boards/ESP32_CAM
    #rename in micropython-camera-driver/src/modcamera.c MP_REGISTER_MODULE(MP_QSTR_camera, mp_module_camera_system); (end) to remove last argument - MP_REGISTER_MODULE(MP_QSTR_camera, mp_module_camera_system, MODULE_CAMERA_ENABLED);
    #and his declaration on ~/esp/micropython/ports/esp32/build-ESP32_CAM/genhdr/moduledefs.h (remove bad (1) argument)
    cp -R $HOME/esp/micropython-camera-driver/boards/ESP32_CAM $HOME/esp/micropython/ports/esp32/boards/ESP32_CAM
    sed -i 's/MP_REGISTER_MODULE(MP_QSTR_camera, mp_module_camera_system, MODULE_CAMERA_ENABLED);/MP_REGISTER_MODULE(MP_QSTR_camera, mp_module_camera_system);/g' $HOME/esp/micropython-camera-driver/src/modcamera.c
}

installNewFirmware(){
    pip3 install esptool
    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 build-ESP32_CAM/firmware.bin
}

if $help; then
    showHelp
else
    if $force ; then
        installRequirements
    fi

    installEspIdf
    if not $generic ; then
        deployESP32Cam
    fi
    deployAndCompileMicroPython

    if $deploy ; then
        installNewFirmware
    fi
fi