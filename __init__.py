import RPi.GPIO as GPIO
import board
import adafruit_dht # Importing a library used for the DHT22 which is the same as our AM2302 
import botbook_mcp3002 as mcp # For MQ-2 smoke sensor

_ledPin = 17
_am2302Pin = board.D2

def createConnection():
    while 1:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            break

        except RuntimeError as error:
            print("Could not establish a connection to the Raspberry Pi")
    
   

def readSensor(sensorType):
    
    if sensorType == "Temperature":
        t = 0
        while t == 0:
            try:
                am2302 = adafruit_dht.DHT22(_am2302Pin, use_pulseio=False)
                t = am2302.temperature
            except RuntimeError as error:
                continue
        
        return t

    elif sensorType == "Humidity":
        h = 0
        while h == 0:
            try:
                am2302 = adafruit_dht.DHT22(_am2302Pin, use_pulseio=False)
                h = am2302.humidity
            except RuntimeError as error:
                continue
        
        return h

    elif sensorType == "Gas": # Seems like we need another chip (MCP 3002) to read the value
        return mcp.readAnalog()

    elif sensorType == "Distance":
        return 0
    elif sensorType == "":
        return 0
    elif sensorType == "":
        return 0
    elif sensorType == "":
        return 0

def powerON(outputType):    

    if outputType == 'LED':
        GPIO.setup(_ledPin, GPIO.OUT)
        GPIO.output(_ledPin, GPIO.LOW) # Turn on LED

    elif outputType == 'Motor':
        return 0

def powerOFF(outputType):

    if outputType == 'LED':
        GPIO.setup(_ledPin, GPIO.OUT)
        GPIO.output(_ledPin, GPIO.HIGH) # Turn off LED
    
    elif outputType == 'Motor':
        return 0