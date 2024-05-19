# Importing Libraries 
import serial 
import time 

# ADJUST SPEED & ANGLE HERE
# speed must be a 2 digit value
SPEED_PERCENTAGE = '20'
SERVO_LEFT_BOUND = '45'
SERVO_RIGHT_BOUND = '135'

def init_arduino():
    # must be COM19
    arduino = serial.Serial(port='COM19', baudrate=115200, timeout=.1) 
    return arduino

def write_read(x, arduino): 
    arduino.write(bytes(x, 'utf-8')) 
    time.sleep(0.05) 
    data = arduino.readline() 
    return data 

if __name__ == "__main__":

    ard = init_arduino()

    while True: 
        num = input("Enter a number: ") # Taking input from user 
        value = write_read(num, ard) 
