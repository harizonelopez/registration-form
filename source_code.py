from tkinter import *
import tkinter as tk

root=Tk()

root.title("@Dev_aladinh ")
root.geometry( )

root.resizable(True,True)

def register_user():
    print("Congrats!!, you are succesfully registerd to SIT101 unit curriculum.")

Label(root,text="SIT101 Course Unit Registration Form.", background = "indigo", font="arial 30").place(x=400, y=60)

Label(text="Name", font=30).place(x=100,y=150)
Label(text="Registration Number", font=30).place(x=100,y=250)
Label(text="Email", font=30).place(x=100,y=350)
Label(text="Gender", font=30).place(x=100,y=550)
Label(text="School of Study", font=30).place(x=100,y=450)

#entry data
nameValue=StringVar()
registrationnumberValue=StringVar()
emailValue=StringVar()
genderValue=StringVar()
schoolofstudyValue=StringVar()

#entry fields
nameEntry=Entry(root,textvariable=nameValue, width=40, bd=2, font=20)
registrationEntry=Entry(root,textvariable=registrationnumberValue, width=40, bd=2, font=20)
emailEntry=Entry(root,textvariable=emailValue, width=40, bd=2, font=20)
schoolofstudyEntry=Entry(root,textvariable=schoolofstudyValue, width=40, bd=2, font=20)

#check gender
checkValue=IntVar
checkbtn=Checkbutton(text="male", font=10, variable=checkValue)
checkbtn.place(x=400, y=550)
checkbtn=Checkbutton(text="Female", font=10, variable=checkValue)
checkbtn.place(x=500, y=550)

nameEntry.place(x=400, y=150)
registrationEntry.place(x=400, y=250)
emailEntry.place(x=400, y=350)
schoolofstudyEntry.place(x=400, y=450)

#check button 
checkValue=IntVar
Checkbtn=Checkbutton(text="Remember me?", font=10, variable=checkValue)
Checkbtn.place(x=600, y=600)

#to add a command to it
register_button = tk.Button(root, text="Register", font=10, background="blue", command = register_user)
register_button.place(x=600, y=650)
               
root.mainloop()
