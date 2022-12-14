# Micropython for ESP32-CAM

Simple tools to get a fresh micropython firmware for esp32-cam.

![Micropython for ESP32-CAM GUI - Screen 1](https://i.ibb.co/hX2KLX9/Captura-desde-2022-12-14-14-34-23.png)

![Micropython for ESP32-CAM GUI - Screen 2](https://i.ibb.co/B3kgGW4/esp32-cam.png)

Internally, the GUI will have scripts, which you're able to use. They will compile and flash a fresh micropython into an ESP32-CAM with the following ![driver](https://github.com/lemariva/micropython-camera-driver)

This will be the most recently firmware to get your MicroPython programs working on ESP32-CAM. 

I recomend develop Thonny or ME editor (which supports micropython and an agile development).

## How to launch

With GUI:

```
python main.py
```

If you want to launch it from console:

```
cd assets/
./arch-compile.sh
```

## Status

Some new features will be available soon. Currently you're able to launch and test the current development version.

Remember, the status of this project is "in development", take it into account. 

## Why

- I want the last revision of Micropython in this board, and this board needs a driver to get camera working. So... here we are.
- Some users want to use this board to pretty projects. And I want users understand all from the begining to the end.
- I would implement the last GitHub improves to offer to user the lastest firmware.
- I want a simple tool for unskilled users. It's not enough (at least for me) known how all works, and it's important all people know how works.

## Problems, problems everywhere

![problems everywhere](https://smarter-ecommerce.com/blog/en/wp-content/uploads/2016/08/feed-problems.gif)

Screen, minicom, picocom, rshell, repl and all adafruit tools will not work by default with this board. Why? Because I just investigate ![in this project](https://github.com/bitstuffing/esp32-telecam) why serial comunication works with Arduino Serial console and why not with other traditionals tools. By the way, I've found some solutions:

To solve the same issue with rshell (good tool recomended in micropython official forum by the oficial MicroPython team developers) :

```
rshell -p /dev/ttyUSB0 --rts false --dtr false
```

If you want to have a easy life, use Thonny (Thonny is a very useful tool for micropython and very known in RPi Pico developers). Please add this configuration in defaults.ini (extracted from ![Thonny's GitHub repo](https://github.com/thonny/thonny/issues/1462)) :

```
[ESP32]
dtr = False
rts = False
```

## License
Powered by @bitstuffing under ![GPLv3](http://www.gnu.org/licenses/GPLv3). 