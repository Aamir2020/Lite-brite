import numpy as np
from PIL import Image

file = open("Color Grid","rb")
color_grid = np.load(file)
#print(color_grid)

final_image = np.array([[[255 for l in range(3)] for m in range(33)] for n in range(10)])


for x in range(0,9,2):
   for y in range(0,33):
        if (y%2) == 0:
            i = int((33*x+ y)/2)
            final_image[x,y,0]=color_grid[i,0]
            final_image[x,y,1]=color_grid[i,1]
            final_image[x,y,2]=color_grid[i,2]
        if (y%2) != 0:
            i = int((33*(x+1) + y)/2)
            final_image[x+1,y,0]=color_grid[i,0]
            final_image[x+1,y,1]=color_grid[i,1]
            final_image[x+1,y,2]=color_grid[i,2]


resized_image = np.array([[[255 for l in range(3)] for m in range(3300)] for n in range(1000)])
for x in range(0,10):
    for y in range(0,33):
        for z in range(100):
            for l in range(100):
                resized_image[100*x+z,100*y+l,0]=final_image[x,y,0]
                resized_image[100*x+z,100*y+l,1]=final_image[x,y,1]
                resized_image[100*x+z,100*y+l,2]=final_image[x,y,2]
       


#final_image = final_image.astype('int8')
resized_image = resized_image.astype('int8')
#im = Image.fromarray(final_image, 'RGB')
im = Image.fromarray(resized_image, 'RGB')
#im = im.resize((330, 100))
im.save('test.png')