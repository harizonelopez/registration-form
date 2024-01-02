from tkinter import *

root=Tk()

root.title("@Dev_aladinh ")
root.geometry( )
root.resizable(True,True)

def Register():
    print("You are succesfully registerd to SIT 100 unit ^'^ ")

Label(root,text="SIT 100 Unit Registration Form", font="arial 40").pack(pady=50)

Label(text="Name", font=30).place(x=100,y=150)
Label(text="Registration Number", font=30).place(x=100,y=250)
Label(text="Email", font=30).place(x=100,y=350)
Label(text="Gender", font=30).place(x=100,y=450)
Label(text="School of Study", font=30).place(x=100,y=550)

#entry
nameValue=StringVar()
registrationnumberValue=StringVar()
emailValue=StringVar()
genderValue=StringVar()
schoolofstudyValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue, width=40, bd=2, font=20)
registrationEntry=Entry(root,textvariable=registrationnumberValue, width=40, bd=2, font=20)
emailEntry=Entry(root,textvariable=emailValue, width=40, bd=2, font=20)
schoolofstudyEntry=Entry(root,textvariable=schoolofstudyValue, width=40, bd=2, font=20)
#genderEntry=Entry(root,textvariable=genderValue, width=40, bd=2, font=20)
#check gender
checkValue=IntVar
checkbtn=Checkbutton(text="male", font=10, variable=checkValue)
checkbtn.place(x=400, y=550)
checkbtn=Checkbutton(text="Female", font=10, variable=checkValue)
checkbtn.place(x=500, y=550)

nameEntry.place(x=400, y=150)
registrationEntry.place(x=400, y=250)
emailEntry.place(x=400, y=350)
#genderEntry.place(x=400, y=450)
schoolofstudyEntry.place(x=400, y=450)

#check button 
checkValue=IntVar
Checkbtn=Checkbutton(text="Remember me?", font=10, variable=checkValue)
Checkbtn.place(x=600, y=600)

Button(text="Register",font=10, background="blue").place(x=600, y=650)
               
root.mainloop()
