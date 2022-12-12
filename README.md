# Micropython for ESP32-CAM

This script will compile and flash a fresh micropython into an ESP32-CAM with the following ![driver](https://github.com/lemariva/micropython-camera-driver)
This will be the most recently base to get your scripts working on ESP32-CAM throw Thonny or ME editor (which supports micropython and an agile development)

## Status

Current status is "in development". Take it into account.

## Why

- I want the last revision of Micropython in this board, and this board needs this driver to get camera working. So... this development has a mandatory requirement.
- I want to use this board to a pretty project that one friend requires to me. And I want he understands all code, what kind of perfect solution will be micropython for that?
- I want to use the last GitHub improves to offer the lastest firmware.

## Problems, problems everywhere

![problems everywhere](https://smarter-ecommerce.com/blog/en/wp-content/uploads/2016/08/feed-problems.gif)

Screen, minicom, picocom, rshell, repl and all adafruit tools will not work by default with this board. Why? Because I just investigate ![in this project](https://github.com/bitstuffing/esp32-telecam) why serial comunication works with Arduino Serial console and why not with other traditionals tools. By the way, I've found a solution:

If you want to have a easy life, use opensource tools like Thonny (Thonny is a very useful tool for micropython and very known in RPi Pico developers). Please add this configuration in defaults.ini (extracted from ![Thonny's GitHub repo](https://github.com/thonny/thonny/issues/1462)) :

```
[ESP32]
dtr = False
rts = False
```

## License
Powered by @bitstuffing under ![GPLv3](http://www.gnu.org/licenses/GPLv3). 