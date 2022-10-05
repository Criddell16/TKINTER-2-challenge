from tkinter import *

window = Tk()

window.title("Km conversions")

def kmTomiles():
    miles = float(e1Value.get())*1.6

    t1.delete("1.0",END)
    t1.insert(END, miles)

def kmTograms():
    grams = float(e1Value.get())*1000

    t2.delete("1.0", END)
    t2.insert(END, grams)

def kmTopounds():
    pounds = float(e1Value.get())*2.20462

    t3.delete("1.0", END)
    t3.insert(END, pounds)

def kmToounces():
    ounces = float(e1Value.get())*35.274

    t4.delete("1.0", END)
    t4.insert(END, ounces)
    
def convert():
    kmTomiles()
    kmTograms()
    kmTopounds()
    kmToounces()


e1Value=StringVar()    
e1 = Entry(window, textvariable=e1Value)
e1.grid(column=1, row=0)


t1 = Text(window,height=1, width=20)
t1.grid(column=0, row=1)

t2 = Text(window,height=1, width=20)
t2.grid(column=0, row=2)

t3 = Text(window,height=1, width=20)
t3.grid(column=0, row=3)

t4 = Text(window,height=1, width=20)
t4.grid(column=0, row=4)

b1 = Button(window, text='Convert', command =convert,
            bg='green', fg='blue')
b1.grid(column=1,row=5, ipadx=20)

L1 = Label(window, text='Miles', fg='blue')
L1.grid(column=1,row=1)

L2 = Label(window, text='Grams', fg='blue')
L2.grid(column=1, row=2)

L3 = Label(window, text='Pounds', fg='blue')
L3.grid(column=1, row=3)

L4 = Label(window, text='Ounces', fg='blue')
L4.grid(column=1, row=4)
        
Lkm = Label(window, text='Enter Km here :', fg='blue')
Lkm.grid(column=0, row=0)


window.mainloop()
