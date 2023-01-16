from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Terminator')
root.iconbitmap('C:\msys64\mingw64.ico')

my_img=ImageTk.PhotoImage(Image.open("ocean-3605547__480.jpg"))
my_Label=Label(image=my_img)
my_Label.grid(row=0,column=0)







button_exit=Button(root,text='Exit Program',command=root.quit)
button_exit.grid(row=1,column=0)    

root.mainloop()