import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))


#A subscriber to subscribe to the topic TEMPERATURE
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Judges") #Giving the client a name
client.connect(mqttBroker)

client.loop_start()
client.subscribe("teams/1007")
client.on_message = on_message
time.sleep(30)
client.loop_end()