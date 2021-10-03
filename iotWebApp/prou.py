import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT) #1
GPIO.setup(20,GPIO.OUT) #2
GPIO.setup(16,GPIO.OUT) #3
GPIO.setup(26,GPIO.OUT) #4
GPIO.setup(18,GPIO.OUT) #shake


def start():
    GPIO.output(21,True)
    GPIO.output(20,True)
    GPIO.output(16,True)
    GPIO.output(26,True)
    print("start")

def drink1():
    print("drink1")
    GPIO.output(21,False)
    time.sleep(1)
    GPIO.output(21,True)
    print("mosza")
 
def drink2():
    print("drink2")
    GPIO.output(20,False)
    time.sleep(1)
    GPIO.output(20,True)
 
def drink3():
    print("drink3")
    GPIO.output(16,False)
    time.sleep(1)
    GPIO.output(16,True)
 
def drink4():
    print("drink4")
    GPIO.output(26,False)
    time.sleep(1)
    GPIO.output(26,True)
    
def drink5():
    print("drink5")
    GPIO.output(21,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(20,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(20,True)
    GPIO.output(16,True)
    GPIO.output(26,True)

def drink6():
    print("drink6")
    GPIO.output(21,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(16,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(20,True)
    GPIO.output(16,True)
    GPIO.output(26,True)

def drink7():
    print("drink7")
    GPIO.output(20,False)
    time.sleep(1)
    GPIO.output(20,True)
    GPIO.output(16,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(20,True)
    GPIO.output(16,True)
    GPIO.output(26,True)

def drink8():
    print("drink8")
    GPIO.output(16,False)
    time.sleep(1)
    GPIO.output(16,True)
    GPIO.output(26,False)
    time.sleep(1)
    GPIO.output(21,True)
    GPIO.output(20,True)
    GPIO.output(16,True)
    GPIO.output(26,True)
            
            
def shake():
    print("shake")
    GPIO.output(18,False)
    time.sleep(3.5)
    GPIO.output(18,True)

def custom1(x):
    print("cus1")
    print(x)
    GPIO.output(21,False)
    time.sleep(x)
    GPIO.output(21,True)

def custom2(x):
    print("cus2")
    print(x)
    GPIO.output(20,False)
    time.sleep(x)
    GPIO.output(20,True)
    
def custom3(x):
    print("cus3")
    print(x)
    GPIO.output(16,False)
    time.sleep(x)
    GPIO.output(16,True)

def custom4(x):
    print("cus4")
    print(x)
    GPIO.output(26,False)
    time.sleep(x)
    GPIO.output(26,True)
