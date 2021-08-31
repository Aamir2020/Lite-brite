import numpy as np
import time
import board
import neopixel
import digitalio
import random



pixel_pin = board.D18
num_pixels = 4
color_information = [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]]
pixels = neopixel.NeoPixel(pixel_pin, num_pixels,auto_write=False)

file = open("gamma_correction", "rb")
gamma = np.load(file)



select0 = digitalio.DigitalInOut(board.D5)
select1 = digitalio.DigitalInOut(board.D6)
select2 = digitalio.DigitalInOut(board.D13)
select3 = digitalio.DigitalInOut(board.D19)

select0.direction = digitalio.Direction.OUTPUT
select1.direction = digitalio.Direction.OUTPUT
select2.direction = digitalio.Direction.OUTPUT
select3.direction = digitalio.Direction.OUTPUT

muxselect0 = digitalio.DigitalInOut(board.D17)
muxselect1 = digitalio.DigitalInOut(board.D4)
muxselect2 = digitalio.DigitalInOut(board.D3)
muxselect3 = digitalio.DigitalInOut(board.D2)

muxselect0.direction = digitalio.Direction.OUTPUT
muxselect1.direction = digitalio.Direction.OUTPUT
muxselect2.direction = digitalio.Direction.OUTPUT
muxselect3.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
#button.pull = digitalio.Pull.UP

s0 = [0,1,0,1,0,1,0,1,0] 
s1 = [0,0,1,1,0,0,1,1,0] 
s2 = [0,0,0,0,1,1,1,1,0] 
s3 = [0,0,0,0,0,0,0,0,1]

rows = 9

signal_reading = [0 for n in range(rows)]
print("The matrix after initializing: " + str(signal_reading))


def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    muxselect0.value = 0
    muxselect1.value = 0
    muxselect2.value = 0
    muxselect3.value = 0
    for i in range(9):
        select0.value = s0[i] 
        select1.value = s1[i] 
        select2.value = s2[i] 
        select3.value = s3[i]
        pixels.fill(color)
        pixels.show()
        time.sleep(wait_ms/1000.0)
       
               
def theaterChase(color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    muxselect0.value = 0
    muxselect1.value = 0
    muxselect2.value = 0
    muxselect3.value = 0
    for j in range(iterations):
        for q in range(3):
            for i in range(0, 9, 3):
                select0.value = s0[i+q] 
                select1.value = s1[i+q] 
                select2.value = s2[i+q] 
                select3.value = s3[i+q]
                pixels.fill(color)
                pixels.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, 9, 3):
                select0.value = s0[i+q] 
                select1.value = s1[i+q] 
                select2.value = s2[i+q] 
                select3.value = s3[i+q]
                pixels.fill((0, 0, 0))
                pixels.show()

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (gamma[pos * 3], gamma[255 - pos * 3], gamma[0])
    elif pos < 170:
        pos -= 85
        return (gamma[255 - pos * 3],gamma[0], gamma[pos * 3])
    else:
        pos -= 170
        return (gamma[0], gamma[pos * 3], gamma[255 - pos * 3])
    

def rainbow(wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(9):
            select0.value = s0[i] 
            select1.value = s1[i] 
            select2.value = s2[i] 
            select3.value = s3[i]
            pixels.fill(wheel((i+j) & 255))
            pixels.show()
        time.sleep(wait_ms/1000.0)
        
def rainbowCycle(wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(9):
            select0.value = s0[i] 
            select1.value = s1[i] 
            select2.value = s2[i] 
            select3.value = s3[i]
            pixels.fill(wheel((int(i * 256 / 9) + j) & 255))
            pixels.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, 9, 3):
                select0.value = s0[i+q] 
                select1.value = s1[i+q] 
                select2.value = s2[i+q] 
                select3.value = s3[i+q]
                pixels.fill(wheel((i+j) % 255))
                pixels.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, 9, 3):
                select0.value = s0[i+q] 
                select1.value = s1[i+q] 
                select2.value = s2[i+q] 
                select3.value = s3[i+q]
                pixels.fill((0, 0, 0))
                pixels.show()
                
    

def Leds(x,y):
    if y == 1:
        pixels.fill((0, 0, 0))
        pixels.show()
        pixels.fill((gamma[color_information [x][0]], gamma[color_information [x][1]], gamma[color_information [x][2]]))
        pixels.show()
    else:
        pixels.fill((0, 0, 0))
        pixels.show()

def current_readings():
    print("----------------------")
    print("Multiplexer readings: ")
    print("----------------------")
    muxselect0.value = 0
    muxselect1.value = 0
    muxselect2.value = 0
    muxselect3.value = 0
    for i in range(rows):
        
        select0.value = s0[i] 
        select1.value = s1[i] 
        select2.value = s2[i] 
        select3.value = s3[i]
        #time.sleep(0.2)
        if button.value == 0:
            signal_reading[i] = 1
            #pixels.fill((0, 0, 100))
            Leds(i , 1) 
            
        else:
            signal_reading[i] = 0
            #pixels.fill((0, 0, 0))
            Leds(i , 0)
    #printing updated matrix
    for j in range(3):
        print(str(signal_reading[j]) + " ", end = '')
    print()
    
    for j in range(3, 6):
        print(str(signal_reading[j]) + " ", end = '')
    print()
    
    for j in range(6, 9):
        print(str(signal_reading[j]) + " ", end = '')
    print()
    
    print("----------------------")
 

try: 
    while True: 
        print ('Color wipe animations.')
        colorWipe((gamma[196], gamma[0], gamma[0]))
        colorWipe((gamma[0], gamma[196], gamma[0]))
        colorWipe((gamma[0], gamma[0], gamma[196]))
        colorWipe((0, 0, 0))
        print ('Theater chase animations.')
        theaterChase((gamma[127], gamma[127], gamma[127]))  
        theaterChase((gamma[127], gamma[0], gamma[0])) 
        theaterChase(( gamma[0], gamma[0], gamma[127]))
        print ('Rainbow animations.')
        rainbow()
        rainbowCycle()
        theaterChaseRainbow()
        current_readings() 
        time.sleep(0.1)
         
except KeyboardInterrupt: 
    print("Ending program")








#s0 = 29 : GPIO 5
#s1 = 31 : GPIO 6
#s2 = 33 : GPIO 13
#s3 = 35 : GPIO 19