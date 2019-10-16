import Adafruit_BBIO.UART as UART
import serial
import time

#UART2: /dev/ttyO2, Rx: P9_22, Tx: P9_21

UART.setup("UART2")

class Beagle:
    def __ini__(self):
        self.temperature
        self.humidity

    def GetTemperature(self):
        with serial.Serial(port = "/dev/ttyO2", baudrate=9600, timeout=None,
            parity=serial.PARITY_NONE, stopbits= serial.STOPBITS_ONE,
            bytesize=8) as ser:
            print(serial)
            print("Serial is open")
            temp = ser.read(2)   #read up to two bytes(tiemout) temperature,hum:
            hum = ser.read(2)
            print('Temperature: {0}'.format(temp))
            print('Humidity: {0}'.format(hum))
            self.temperature = temp.decode("utf-8")
            self.humidity = hum.decode("utf-8")

#UART1: /dev/ttyO1, Rx: P9_26, Tx: P9_24
#UART2: /dev/ttyO2, Rx: P9_22, Tx: P9_21
#UART4: /dev/ttyO4, Rx: P9_11, Tx: P9_13
#UART5: /dev/ttyO5, Rx: P8_38, Tx: P8_37
