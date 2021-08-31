import numpy as np
from PIL import Image
import math

def Color_circle(RED,GREEN,BLUE):

    data = np.array([[[0 for l in range(4)] for m in range(40)] for n in range(40)])
    data = data.astype('int8') 
    # image = Image.open('circle.png')
    # image = image.convert('RGBA')
    # image = image.resize((10, 10), Image.ANTIALIAS)
    # data = np.array(image)
    for x in range(40):
        for y in range(40):
            data[x,y,3] = 0
            if pow((x-20),2) + pow((y-20),2) < pow(19,2):
                data[x,y,0] = RED
                data[x,y,1] = GREEN
                data[x,y,2] = BLUE
                data[x,y,3] = 255
        #     r= data[x,y,0]
        #     g= data[x,y,1]
        #     b= data[x,y,2]
        #     a= data[x,y,3]
        #     print("("+str(r)+","+str(g)+","+str(b)+","+str(a)+") ",end='')
        # print("")
                
    im = Image.fromarray(data,'RGBA')
    im.save('circle2.png')
    
    # for x in range(39):
    #     for y in range(39):
    #         red, green, blue = data[x,y,0], data[x,y,1], data[x,y,2]

    # r1, g1, b1 = 55, 55, 55 # Original value
    # r2, g2, b2 = 30, 57, 79 # Value that we want to replace it with

    # red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    # mask = (red == r1) & (green == g1) & (blue == b1)
    # data[:,:,:3][mask] = [r2, g2, b2]
    
    #image_file = 'circle.png'.py.replace(".png","")
    
    #print(data)



# for x in range(49):
#     for y in range(49):
#         current_color = image.getpixel( (x,y) )
            
#         picture.putpixel( (x,y), new_color)
