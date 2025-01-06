import serial
import time
import datetime
from discord_webhook import DiscordWebhook
import os
from dotenv import load_dotenv

load_dotenv()


# Configuration
COM_PORT = "/dev/ttyUSB0"  # Replace with your COM port (e.g., COM3, /dev/ttyUSB0)
BAUD_RATE = 9600   # Set to match your Arduino baud rate
rep = 0
ctr = datetime.datetime.now()
hook = os.getenv('webhook')

def count(num):
    global rep
    rep+= num
    return rep

def notify():
    global ctr
    message = f"Your system shutting down due to power loss on {ctr.day}/{ctr.month}/{ctr.year} at {ctr.hour}:{ctr.minute}:{ctr.second}"
    webhook = DiscordWebhook(url=hook, content=message)
    webhook.execute()
    print(message)

try:
    # Open the serial connection
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {COM_PORT} at {BAUD_RATE} baud.")
    
    # Continuously read data from the serial port
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            line = ser.readline().decode("utf-8").strip()  # Read and decode a line
            print(line)  # Print to console
            if line:
                check = count(1)
                print(check)
                if check > 9:
                    print("terminate")
                    notify()
                    os.system("shutdown")
                    break


except KeyboardInterrupt:
    print("\nStopping data logging...")
except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
    print("Serial port closed.")
