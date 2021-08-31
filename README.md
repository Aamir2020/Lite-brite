### Lite Brite Python Scripts ###

Python scripts for communicating with LED PCB of the Lite Brite with a Raspberry Pi

### lite_brite.py ###

A script to light the LEDs green when the button is pressed.

Run `sudo python3 lite_brite.py`

By default, GPIO pin 18 is used for the LED pin and GPIO pin 23 is used for the switch pin. These can be changed. However, only GPIO pins 10, 12, 18 or 21 seem to work for the LED pin.

### switch.py ###

A script to test that the switch is working. When the button is not pressed, '1' will be printed to the terminal. When the button is pressed, '0' will be printed to the terminal.

Run `sudo python3 switch.py`

By default, GPIO pin 23 is used for the switch.


#### simple_test.py ####

A test for making sure the LEDs are working.

Run `sudo python3 simple_test.py`

The LEDs will perform the following pattern: red, green, blue, rainbow.

The GPIO pin for LED is set to 18 by default.