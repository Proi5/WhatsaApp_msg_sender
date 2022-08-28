from tokenize import Number
from turtle import width
import pyautogui
import time
from tkinter import *
##Masseg Box
root = Tk()
root.title("Msg Box")
def Clebox(e):
    Ti.delete(0,"end")
def Clebox1(e):
    Nu.delete(0,"end")
def Clebox2(e):
    Masseg.delete(0,"end")
Ti = Entry(root,width=40,borderwidth=15,)
Nu = Entry(root,width=40,borderwidth=15,)
Masseg = Entry(root,width=40,borderwidth=15,)
Masseg.insert(0,"Messege")
Ti.insert(0,"Time to start(in second)")
Nu.insert(0,"Number of msg want to send")
Ti.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
Nu.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
Masseg.grid(row=4,column=0,columnspan=3,padx=10,pady=10)
##To delete the word
Ti.bind("<FocusIn>",Clebox)
Nu.bind("<FocusIn>",Clebox1)
Masseg.bind("<FocusIn>",Clebox2)
##Command for button 
def Click():
    Time = int(Ti.get())
    Number = int(Nu.get())
    time.sleep(Time)
    for i in range(Number):
        pyautogui.write(Masseg.get())
        pyautogui.press("enter")
##Button Box
Button1 = Button(root,text="Send",command=Click,width=10,borderwidth=5,padx=10,pady=5)
Button1.grid(row=5,column=1,)
##loop for root
root.mainloop()
