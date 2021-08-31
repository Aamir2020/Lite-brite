from tkinter import  *
from lite_brite_v3 import initialization,Follow_the_leader_Mode, Match_Mode, Free_Mode
from Make_picture import Create_Image

def Match_Mode_Image():
    
    new_window = Tk()
    new_window.title("Select one opton")

    option1 = Button(root, text = "Load existing image", font=(33), command = Match_Mode)
    option2 = Button(root, text = "Create new image", font=(33), command = Create)
    # option1 = Button(new_window, text = "Load existing image", font=(33))
    # option2 = Button(new_window, text = "Create new image", font=(33))

    option1.pack()
    option2.pack()

    new_window.geometry("250x150")
    new_window.mainloop()


def Create():
    Create_Image()
    Match_Mode()


root = Tk()
root.title("File selector")


program1 = Button(root, text = "Follow the leader Mode", font=(33), command = lambda:[initialization(),Follow_the_leader_Mode()])
program2 = Button(root, text = "Match Mode", font=(33), command = lambda:[initialization(),Match_Mode_Image()])
program3 = Button(root, text = "Free Mode", font=(33), command = lambda:[initialization(),Free_Mode()])

# program1 = Button(root, text = "Follow the leader Mode", font=(33))
# program2 = Button(root, text = "Match Mode", font=(33), command = Match_Mode_Image)
# program3 = Button(root, text = "Free Mode", font=(33))

program1.pack()
program2.pack()
program3.pack()



root.geometry("250x150")
root.mainloop()

