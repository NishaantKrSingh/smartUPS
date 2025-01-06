## How to use
1. Connect a pull-down resistor of anywhere between 10kΩ to 100kΩ to avoid reading the floating state values which causes it to read random electrical noises between pin 2 and GND.
2. Connect the wires from the buzzer of your UPS to a 10kΩ resistor or any resistor that drops the voltage enough to make it safe to work with Arduino i.e. between 1V to 5V will be enough.
3. Put the `read.ino` code on Arduino IDE and flash it to your Arduino.
4. Run the `main.py` python code to read the COM port which will perform the actions like Sending notification via Discord webhooks and shutting down your PC.

Dont forget to rename `.env.example` as `.env` and add your Discord webhooks URL there.