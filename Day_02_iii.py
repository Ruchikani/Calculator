from tkinter import *

window=Tk()
window.geometry("400x400")
window.title("Digital Clock")

lb1 = Label(window,text="First Number",font=15)
lb1.pack()

txt1 = Text(window,height=2,width=30,font=10)
txt1.pack()

lb2 = Label(window,text="Second Number",font=15)
lb2.pack()

txt2 = Text(window,height=2,width=30,font=10)
txt2.pack()

def myadd():
    n1 = int(txt1.get("1.0","end-1c"))
    n2 = int(txt2.get("1.0","end-1c"))
    print(n1+n2)

def mysubstract():
    n1 = int(txt1.get("1.0","end-1c"))
    n2 = int(txt2.get("1.0","end-1c"))
    print(n1-n2)

def mymultiply():
    n1 = int(txt1.get("1.0","end-1c"))
    n2 = int(txt2.get("1.0","end-1c"))
    print(n1*n2)

def mydivide():
    n1 = int(txt1.get("1.0","end-1c"))
    n2 = int(txt2.get("1.0","end-1c"))
    print(n1/n2)

btn1 = Button(window,command=myadd,text="Add",font=10,height=2,width=20)
btn1.pack()

btn2 = Button(window,command=mysubstract,text="Substract",font=10,height=2,width=20)
btn2.pack()

btn3 = Button(window,command=mymultiply,text="Multiply",font=10,height=2,width=20)
btn3.pack()

btn4 = Button(window,command=mydivide,text="Divide",font=10,height=2,width=20)
btn4.pack()


window.mainloop()
