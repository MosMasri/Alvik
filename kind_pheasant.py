from arduino import *
from arduino_alvik import ArduinoAlvik

alvik = ArduinoAlvik()

def setup():
    alvik.begin()
    delay(2000)  # even wachten voor start

def loop():

    alvik.set_wheels_speed(50,50)   
    delay(500)
    alvik.set_wheels_speed(-50,-50) 
    delay(500)

    
    alvik.set_wheels_speed(0,100)    
    delay(500)
    alvik.set_wheels_speed(100,0)    
    delay(500)
    alvik.set_wheels_speed(0,100)    
    delay(500)
    alvik.set_wheels_speed(100,0)    
    delay(500)
    alvik.set_wheels_speed(0,100)    
    delay(500)
    alvik.set_wheels_speed(100,0)    
    delay(500)


    alvik.set_wheels_speed(50,50)   
    delay(500)
    alvik.set_wheels_speed(-50,-50) 
    delay(500)

    alvik.set_wheels_speed(80,-80)
    delay(1500)
  
    alvik.set_wheels_speed(-50,-50) 
    delay(1000)
  

  
    alvik.set_wheels_speed(80,-80)
    delay(1500)


def cleanup():
    alvik.stop()

start(setup, loop, cleanup)