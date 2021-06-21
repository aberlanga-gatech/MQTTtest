"""
# Made by Alfredo Berlanga
# alfredo@propelland.com
Version 1.2.1
Based on the Paho documentation example codes
"""

import sys
import paho.mqtt.client as mqtt
import time
import constants


# connection event
def on_connect(client, data, flags, rc):
    if rc == 0:
        print("Connection successful")
    else:
        print(f"Connection failed with code {rc}")


# callback from when PUBLISH is received from server
def message_function(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print(f"topic: {message.topic} message: {msg}")


# function to check temperature of probe
def check_temperature():
    # pholder code for checking temperature
    temperature = "19 Celcius"
    return temperature


# function to check pressure of probe
def check_pressure():
    # pholder code for checking pressure
    pressure = "3 Pa"
    return pressure


# function to broadcast kill transmission
def finish_line():
    sender.publish(constants.BREAK_TOPIC, constants.BREAK_TOPIC)
    sys.exit()


sender = mqtt.Client("Underwater_Probe_Client")  # sender client init
sender.connect(constants.SERVER_URL, constants.PORT, 60)  # connect to server

# data log setup
count = 0
tempLog = []
presLog = []

# main loop
while True:
    # m = input()
    # sender.publish(constants.TEMPERATURE_TOPIC, m)
    temperature = check_temperature()
    tempLog[count] = str(count) + " seconds: " + temperature

    pressure = check_pressure()
    presLog[count] = str(count) + " seconds: " + pressure

    sender.publish(constants.TEMPERATURE_TOPIC, temperature)
    sender.publish(constants.PRESSURE_TOPIC, pressure)
    time.sleep(1)
    count = count + 1
