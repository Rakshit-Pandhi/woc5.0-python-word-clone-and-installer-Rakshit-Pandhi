# Checkpoint One --> Bold,Underline and Italics Label
from tkinter import *

root=Tk()

bold_Label=Label(root,text="Winter of Code",font=('Helvetica',18,"bold"))
underline_Label=Label(root,text="Winter of Code",font=('Helvetica',15,"underline"))
italics_Label=Label(root,text="Winter of Code",font="italic")

bold_Label.grid(row=0,column=0)
underline_Label.grid(row=1,column=0)
italics_Label.grid(row=2,column=0)

root.mainloop()

# Checkpoint Two --> Retrieve value entered in the the input box
from tkinter import *

root=Tk()

f=Entry(root,width=25,fg="white",bg="dark green",borderwidth=7,relief="ridge")
f.pack()
   

def myClick():
    myLabel=Label(root,text=f.get(),fg="red")           
    myLabel.pack()
        

myButton=Button(root,text="Submit",command=myClick,fg="yellow",bg="black")
myButton.pack()
      

root.mainloop()

# Checkpoint 3 --> Clear the input entered in the box
from tkinter import *

root=Tk()

def clear():
    i.delete(0,END)

i=Entry(root,width=35,borderwidth=8,bg="pink",fg="black")
i.grid(row=0,column=0)

my_clear=Button(root,text="CLEAR",command=clear,borderwidth=6,bg="purple",fg="orange",font=('Times',15,"underline"))
my_clear.grid(row=1,column=0)

root.mainloop()

# Checkpoint 4 --> Change a text label's font size and style 
from tkinter import *

root=Tk()

def sty_chg():
    my_Label.config(fg="red",font=('Times',19,"bold"))  # Config function helps changing the font size and style 

my_Label=Label(root,text="Python Tkinter",fg="blue")
my_Label.pack()

my_button=Button(root,text="Change Style",command=sty_chg,bg="red")
my_button.pack()

root.mainloop()