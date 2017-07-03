import os 
from Tkinter import *
root = Tk(className ="My first GUI")
root.geometry("300x300")
root.configure(background='grey')

svalue = StringVar() # defines the widget state as string
w = Entry(root,textvariable=svalue) # adds a textarea widget
w.pack()


# function handling
def act():
    print "you entered"
    if svalue.get() =='q':
        root.quit()
    print '%s' % svalue.get()
foo = Button(root,text="Press Me", command=act)
foo.pack()

# event binding
def left(event):   
    print 'LEFT '
def mid(event):
    print 'MIDDLE '
def rig(event):
    print 'RIGHT '
frame = Frame(root, width=300, height=200, bg='blue')

frame.bind('<Button-1>', left) 
frame.bind('<Button-2>', mid) 
frame.bind('<Button-3>', rig)
frame.pack()

# image upload
#print os.getcwd()
photo = PhotoImage(file='/usr/local/google/home/kumanjay/Downloads/Roster-Sphinx.png')
lable = Label(root, image=photo)
lable.pack()




root.mainloop()





# Object Oriented
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()






