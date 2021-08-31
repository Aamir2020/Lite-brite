from tkinter import  *
from tkinter import colorchooser
import numpy as np
from PIL import ImageTk, Image


def Create_Image():
    led_modules = 165
    dimension = 330

    root = Tk()
    root.title("Lite-Brite UI")
    topframe = Frame(root,bg='#383838')
    topframe.pack()
    bottomframe = Frame(root, bg="black")
    bottomframe.pack( side = BOTTOM, fill = X)

    color_grid = np.array([[0 for m in range(3)] for n in range(led_modules)])

    circle = Image.open('circle.png')

    my_circle = ImageTk.PhotoImage(circle)


    def save_array(color_grid):
        #global color_grid
        color_grid = color_grid.astype(int)
        file = open("Color Grid","wb")
        np.save(file, color_grid)
        file.close
        root.destroy()

    def Color_circle(RED,GREEN,BLUE):

        data = np.array([[[0 for l in range(4)] for m in range(40)] for n in range(40)])
        data = data.astype('int8') 
        
        for x in range(40):
            for y in range(40):
                data[x,y,3] = 0
                if pow((x-20),2) + pow((y-20),2) < pow(19,2):
                    data[x,y,0] = RED
                    data[x,y,1] = GREEN
                    data[x,y,2] = BLUE
                    data[x,y,3] = 255
        

        im = Image.fromarray(data,'RGBA')
        im.save('circle2.png')

    def choose_color(index,color_grid):
        #global color_grid
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        if color_code != (None,None):
            # print(color_code[0])
            color_grid[index] = color_code[0]
            red, green, blue = color_code[0]
            Color_circle(red,green,blue)
            circle2 = Image.open('circle2.png')
            my_circle2 = ImageTk.PhotoImage(circle2)
            globals()["button" + str(index)].config(image=my_circle2)
            globals()["button" + str(index)].photo_ref = my_circle2
        

    for x in range(led_modules):
        globals()["button" + str(x)] = Button(topframe, image = my_circle, borderwidth=0,bg='#383838',font=("Courier", 22),command= lambda m=x: choose_color(m,color_grid))

    for z in range(0,9,2):
        for y in range(0,33):
            if (y%2)==0:
                globals()["button" + str(int((33*z+ y)/2))].grid(row=z, column=y, pady=5, padx=2)
            if (y%2)!=0:
                globals()["button" + str(int((33*(z+1) + y)/2))].grid(row=z+1, column=y, pady=5, padx=2)

    savebutton = Button(bottomframe, text="save", fg="white",bg="green",font=("Courier", 30),command= lambda : save_array(color_grid))
    savebutton.pack()


    root.mainloop()

Create_Image()