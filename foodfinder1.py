from tkinter import *
# PIL allows for images
from PIL import ImageTk, Image


root = Tk()
root.title('Version 1.0 Food Finder')
#Find an .ico image for app icon if able and save to same folder here
#root.iconbitmap(".ico file name here")

#Adding a single image to this potentiall food?
'''
my_img = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
screen_image = Label(image= my_img)
screen_image.pack()
'''


#For adding multiple images
'''
my_img1 = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
my_img2 = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
my_img3 = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
my_img4 = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
my_img5 = ImageTk.PhotoImage(Image.open(".jpg IMage name here"))
'''
#Adding THem to a list
#image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

#Creating a entry widget
hungry = Entry(root, width = 40)
hungry.pack()
hungry.insert(0, "Are you hungry? y/n")


def nextImage():
    return

def previousImage():
    return 

#This is function created for clicking the button
def myClick():
    myLable = Label(root, text = "You clicked the button!")
    myLable.pack()

#Starting Header Label
headerLabel = Label(root, "Hey you want food?") # .grid(row = 0, column = 0)
headerLabel.pack()


mybutton = Button(root, text = "CLick Me!", command = myClick() )  # Grey out button: state = DISABLED
# headerLabel.pack()
# These change the shape of a button: padx= 30, pady = 30


# Quit Button
button_quit = Button(root, text="Exit", command= root.quit)

root.mainloop()