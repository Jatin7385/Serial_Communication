from struct import pack
import serial.tools.list_ports
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

#A publisher to publish the temperature inside the home
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Team_Sammard_Ground_Station") #Giving the client a name
client.connect(mqttBroker)

ports = serial.tools.list_ports.comports()

serialInst = serial.Serial()


portList = []
i = 0
print("Select a port")
for port in ports:
    portList.append(str(port))
    print("Option",i+1," : ",str(port))
    i+=1

val = int(input("Choose one of the options displayed above : "))

com = portList[val-1]

serialInst.baudrate = 9600
serialInst.port = com[0:4]
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline().decode('utf-8')
        print(packet)
        #Publishing packet to topic 
        client.publish("teams/1007",packet)
        print("Just published " + packet + " to Topic teams/1007")
        time.sleep(1)
