"""
# Made by Alfredo Berlanga
# alfredo@propelland.com
Version 1.2.0
Based on the Paho documentation example codes
"""


import paho.mqtt.client as mqtt
import time
import constants


# connection event callback
def on_connect(client, data, flags, rc):
    if rc == 0:  # connection successful
        print("Connection successful")
    else:  # catch connection unsuccessful
        print(f"Connection failed with code {rc}")


# callback from when PUBLISH is received from server
def message_function(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))  # get message as string
    if msg == constants.BREAK_TOPIC:  # catch end transmission conditions
        receiver.loop_stop()
    else:
        print(f"topic: {message.topic} message: {msg}")  # display messages


receiver = mqtt.Client("Logger_of_Data")  # ID of client
receiver.connect(constants.SERVER_URL, constants.PORT, 60)  # connection
receiver.subscribe(constants.TEMPERATURE_TOPIC)  # subscribe to temp topic
receiver.subscribe(constants.PRESSURE_TOPIC)  # subscribe to pressure topic
receiver.on_message = message_function  # assign on message receive callback
receiver.on_connect = on_connect  # assign on connection callback
receiver.loop_start()  # start main loop

# Main loop
while True:
    time.sleep(1)
