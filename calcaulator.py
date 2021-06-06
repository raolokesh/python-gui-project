from tkinter import *

root = Tk()
root.title("Simple Calculator")

#Lets make the input to show first
e = Entry(root,fg='blue',borderwidth=5,width=35)
e.grid(row=0,column=0,columnspan=3)

def clickbutton(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def clearbutton():
    e.delete(0,END)
    global first_no
    first_no=0
global first_no
first_no = 0

def add_button():
    first_number = e.get()
    global first_no
    first_no += int(first_number)
    e.delete(0,END)
    



def equalbutton():
    second_no = int(e.get())
    e.delete(0,END)
    total = first_no+second_no
    e.insert(0,total)

#define button
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda: clickbutton(1))
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda: clickbutton(2))
button_3 = Button(root,text='3',padx=40,pady=20,command=lambda: clickbutton(3))
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda: clickbutton(4))
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda: clickbutton(5))
button_6 = Button(root,text='6',padx=40,pady=20,command=lambda: clickbutton(6))
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda: clickbutton(7))
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda: clickbutton(8))
button_9 = Button(root,text='9',padx=40,pady=20,command=lambda: clickbutton(9))
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda: clickbutton(0))

button_add = Button(root,text='+',pady=20,padx=39,command=add_button)
button_clear = Button(root,text="clear",padx=79,pady=20,command= clearbutton)
button_equal = Button(root,text="=",pady=20,padx=89,command=equalbutton)

# show button using grid
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()
