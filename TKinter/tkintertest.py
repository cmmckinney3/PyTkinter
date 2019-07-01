from tkinter import *


window=Tk()
text = Text(window)


def kg_conversion():
    kg_to_grams = float(e1_value.get())*1000
    kg_to_pounds = float(e1_value.get())*2.20462
    kg_to_ounces = float(e1_value.get())*35.274
    t1.insert(END,kg_to_grams)
    t2.insert(END,kg_to_pounds)
    t3.insert(END,kg_to_ounces)


lab1=Label(window,text="Kg")
lab1.grid(row=0,column=0)

b1=Button(window,text="Convert",command=kg_conversion)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

lab2=Label(window,text="Grams")
lab2.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=2,column=0)

lab3=Label(window,text="Pounds")
lab3.grid(row=1,column=1)
t2=Text(window,height=1,width=20)
t2.grid(row=2,column=1)

lab4=Label(window,text="Ounces")
lab4.grid(row=1,column=2)
t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

window.mainloop()
