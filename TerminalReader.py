from serial import *
import sys
try:
        ser=Serial(04)
        print("port opened")
        #ser.stopbits=2
        while 1:
            data=ser.read()
            sys.stdout.write(data.decode())

except:
        ser.close()