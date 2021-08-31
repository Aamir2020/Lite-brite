# Importing the required modules
import numpy as np
import board
import neopixel
import digitalio
import time
from random import randint
from random import choice


def initialization():
    # The led data is sent from the pin 12 (GPIO 18)
    pixel_pin = board.D18
    # Each led modules has 4 leds
    num_pixels = 4
    global pixels
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels,auto_write=False)
    global select0,select1,select2,select3,muxselect0,muxselect1,muxselect2,muxselect3
    # The selector for multiplexing between the 16 leds
    select0 = digitalio.DigitalInOut(board.D5)
    select1 = digitalio.DigitalInOut(board.D6)
    select2 = digitalio.DigitalInOut(board.D13)
    select3 = digitalio.DigitalInOut(board.D19)

    # Making the selectors an output
    select0.direction = digitalio.Direction.OUTPUT
    select1.direction = digitalio.Direction.OUTPUT
    select2.direction = digitalio.Direction.OUTPUT
    select3.direction = digitalio.Direction.OUTPUT

    #The selector for muliplexing between the 11 multiplexers
    
    muxselect0 = digitalio.DigitalInOut(board.D17)
    muxselect1 = digitalio.DigitalInOut(board.D4)
    muxselect2 = digitalio.DigitalInOut(board.D3)
    muxselect3 = digitalio.DigitalInOut(board.D2)

    # Making the selectors an output
    muxselect0.direction = digitalio.Direction.OUTPUT
    muxselect1.direction = digitalio.Direction.OUTPUT
    muxselect2.direction = digitalio.Direction.OUTPUT
    muxselect3.direction = digitalio.Direction.OUTPUT

    # Each of the 11 buttons are connected to their own pins

    global buttonM0,buttonM1,buttonM2,buttonM3,buttonM4,buttonM5,buttonM6
    global buttonM7,buttonM8,buttonM9,buttonM10
    
    # pin 16 (GPIO 23) or M4 on header board
    buttonM0 = digitalio.DigitalInOut(board.D23)
    # pin 26 (GPIO 7) or M8 on header board
    buttonM1 = digitalio.DigitalInOut(board.D7)
    # pin 24 (GPIO 8) or M7 on header board
    buttonM2 = digitalio.DigitalInOut(board.D8)
    # pin 36 (GPIO 16) or M10 on header board
    buttonM3 = digitalio.DigitalInOut(board.D16)
    # pin 32  (GPIO 12) or M9 on header board
    buttonM4 = digitalio.DigitalInOut(board.D12)
    # pin 37  (GPIO 26) or M22 on header board
    buttonM5 = digitalio.DigitalInOut(board.D26)
    # pin 23 (GPIO 11) or M21 on header board
    buttonM6 = digitalio.DigitalInOut(board.D11)
    # pin 21 (GPIO 9) or M20 on header board
    buttonM7 = digitalio.DigitalInOut(board.D9)
    # pin 19 (GPIO 10) or M19 on header board
    buttonM8 = digitalio.DigitalInOut(board.D10)
    # pin 15 (GPIO 22) or M18 on header board
    buttonM9 = digitalio.DigitalInOut(board.D22)
    # pin 13 (GPIO 27) or M17 on header board
    buttonM10 = digitalio.DigitalInOut(board.D27)

    # Set all of them to input
    buttonM0.direction = digitalio.Direction.INPUT
    buttonM1.direction = digitalio.Direction.INPUT
    buttonM2.direction = digitalio.Direction.INPUT
    buttonM3.direction = digitalio.Direction.INPUT
    buttonM4.direction = digitalio.Direction.INPUT
    buttonM5.direction = digitalio.Direction.INPUT
    buttonM6.direction = digitalio.Direction.INPUT
    buttonM7.direction = digitalio.Direction.INPUT
    buttonM8.direction = digitalio.Direction.INPUT
    buttonM9.direction = digitalio.Direction.INPUT
    buttonM10.direction = digitalio.Direction.INPUT

    # S3 is the least significant and s0 is the most significant
    global s0,s1,s2,s3
    s0 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
    s1 = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1] 
    s2 = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1] 
    s3 = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

    # ms3 is the least significant and ms0 is the most significant
    global ms0,ms1,ms2,ms3
    ms0 = [0,1,0,1,0,1,0,1,0,1,0]
    ms1 = [0,0,1,1,0,0,1,1,0,0,1]
    ms2 = [0,0,0,0,1,1,1,1,0,0,0]
    ms3 = [0,0,0,0,0,0,0,0,1,1,1]

    # total number of rows and columns on the grid
    global rows,column
    rows = 10
    column = 33

    global signal_reading
    signal_reading = [["-" for m in range(33)] for n in range(10)]


    file = open("Color Grid","rb")
    global color_information
    color_information = np.load(file)
    file = open("gamma_correction", "rb")
    global gamma
    gamma = np.load(file)
    global main_color
    main_color = [[0,0,0],[255,255,255],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255],
            [192,192,192],[128,128,128],[128,0,0],[128,128,0],[0,128,0],[128,0,128],[0,128,128],[0,0,128]]
    global coordinate
    coordinate = [[0 for m in range(2)] for n in range(165)]
    i=0

    for x in range(0,10):
        for y in range(0,33):
            if (x%2)==0 and (y%2)==0:
                coordinate[i][0] = x
                coordinate[i][1] = y
                i += 1
            elif (x%2)!=0 and (y%2)!=0:
                coordinate[i][0] = x
                coordinate[i][1] = y 
                i += 1

    #print("The matrix after initializing: " + str(signal_reading)) 

def grid_math(x,y):
    b = x+int(y/(32-x))
    a = int((y+x)/2) - 16
    if a < 0:
        a = int((y+x)/2)
    return b , a

def Leds(b,a,brightness):
    index = b*16+a
    pixels.fill((0, 0, 0))
    pixels.show()
    pixels.fill((gamma[color_information [index][0]]*brightness, gamma[color_information [index][1]]*brightness, gamma[color_information [index][2]]*brightness))
    pixels.show()
    

def selector(b,a):
    muxselect0.value = ms0[b]
    muxselect1.value = ms1[b]
    muxselect2.value = ms2[b]
    muxselect3.value = ms3[b]
    select0.value = s0[a]
    select1.value = s1[a]
    select2.value = s2[a]
    select3.value = s3[a]

def random():
    global coordinate
    random_row, random_column= choice(coordinate)
    coordinate.remove([random_row,random_column])
    return random_row, random_column

def current_readings():
    print("----------------------")
    print("Multiplexer readings: ")
    print("----------------------")
   
    for x in range(0,9,2):
        for y in range(0,33):
            if (y%2) == 0:
                b, a = grid_math(x,y)
                selector(b,a)

                # Make changes to the selector board som  that a single button variable is used
                if globals()["buttonM" + str(b)].value == 0:
                    signal_reading[x][y] = 1
                    Leds(b,a,1)
                
                else:
                    
                    signal_reading[x][y] = 0
                    Leds(b,a,0)

            if (y%2)!=0:
                b, a = grid_math(x+1,y)
                selector(b,a)


                if globals()["buttonM" + str(b)].value == 0:
                    signal_reading[x+1][y] = 1
                    Leds(b,a,1)
                
                else:
                    signal_reading[x+1][y] = 0
                    Leds(b,a,0)
    
    #printing updated matrix
    for i in range(10):
        for j in range(33):
            print(str(signal_reading[i][j]), end = '')
        print()

    print("----------------------")

  
def Follow_the_leader_Mode():    
    start = time.time()
    for i in range(165):
        row , column = random()
        b, a = grid_math(row,column)
        selector(b,a)
        pixels.fill(main_color[randint(0,15)])
        pixels.show()
        while(globals()["buttonM" + str(b)].value != 0):
            if (start+300>time.time()):
                return
            
          
    
def Match_Mode():
    start = time.time()
    for x in range(0,9,2):
        for y in range(0,33):
            if (y%2) == 0:
                b, a = grid_math(x,y)
                selector(b,a)
                Leds(b,a,0.3)
                
            if (y%2) != 0:
                b, a = grid_math(x+1,y)
                selector(b,a)
                Leds(b,a,0.3)
    while (True):
        for x in range(0,9,2):
            for y in range(0,33):
                if (y%2) == 0:
                    b, a = grid_math(x,y)
                    selector(b,a) 

                    if globals()["buttonM" + str(b)].value == 0:
                        if not_pressed == True:
                            signal_reading[x][y] = 1
                            Leds(b,a,1)
                    
                    else:
                        not_pressed = True
                        signal_reading[x][y] = 0
                        Leds(b,a,0.3)

                if (y%2)!=0:
                    b, a = grid_math(x+1,y)
                    selector(b,a)

                    if globals()["buttonM" + str(b)].value == 0:
                        if not_pressed == True:
                            signal_reading[x+1][y] = 1
                            Leds(b,a,1)
                        not_pressed = False
                    
                    else:
                        not_pressed = True
                        signal_reading[x+1][y] = 0
                        Leds(b,a,0.3)
        if (start+300>time.time()):
                return                     

def Free_Mode():
    start = time.time()
    while (True):
        for x in range(0,9,2):
            for y in range(0,33):
                
                if (y%2) == 0:
                    b, a = grid_math(x,y)
                    selector(b,a)

                    if globals()["buttonM" + str(b)].value == 0:
                        if not_pressed == True:
                            pixels.fill(main_color[randint(0,15)])
                            pixels.show()    
                        not_pressed = False
                    else:
                        not_pressed = True
                        pixels.fill((0, 0, 0))
                        pixels.show() 

                if (y%2)!=0:
                    b, a = grid_math(x+1,y)
                    selector(b,a)

                    if globals()["buttonM" + str(b)].value == 0:
                        if not_pressed == True:
                            pixels.fill(main_color[randint(0,15)])
                            pixels.show()
                        not_pressed = False
                    else:
                        not_pressed = True
                        pixels.fill((0, 0, 0))
                        pixels.show()
        if (start+300>time.time()):
                    return









#s0 = 29 : GPIO 5
#s1 = 31 : GPIO 6
#s2 = 33 : GPIO 13
#s3 = 35 : GPIO 19