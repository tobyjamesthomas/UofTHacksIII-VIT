'''
Created on 2011-12-02

@author: Bobby Wood
'''

## import the serial library
import serial

## Boolean variable that will represent
## whether or not the arduino is connected
connected = False

serialPath = '/dev/tty.usbmodem1421'

## open the serial port that your ardiono
## is connected to.
ser = serial.Serial(serialPath, 9600)

## loop until the arduino tells us it is ready
while not connected:
    serin = ser.read()
    connected = True

def inputToSerial(array):
    inputString = ''
    for i in range(len(array)):
        for j in range(len(array[0])):
            inputString += str(array[i][j]) + ','
    return inputString

arrayTest = [[200,200,200],[200,200,200],[200,200,200]]

## Tell the arduino to blink!
ser.write(inputToSerial(arrayTest))

## Wait until the arduino tells us it
## is finished blinking
while ser.read() == '1':
    ser.read()

## close the port and end the program
ser.close()
