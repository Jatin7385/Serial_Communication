import serial.tools.list_ports

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