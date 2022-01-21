from tkinter import *

window = Tk()

window.title('BMI Calculator')
window.geometry("500x500")
window.configure(bg='lightcyan')

def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100
    bmi = weight/(height*height)
    bmi = round(bmi,1)
    name = username.get()
    result_label.destroy()
    msg = ""

    if bmi<18.5:
        msg=" are underweight"
    elif bmi>18.5 and bmi<=24.9:
        msg=" are in normal range"
    elif bmi>25 and bmi<=29.9:
        msg=" are overweight"
    elif bmi>30:
        msg=" are obese"
    else:
        msg="Something went wrong"

    output_msg = Label(result_frame,text=name+", your BMI is "+str(bmi)+" and "+msg,bg="lightcyan",font=("Calibri",15),width=42)
    output_msg.place(x=20,y=40)
    output_msg.pack()

heading_label= Label(window,text="BMI CALCULATOR",fg="black",bg="lightcyan",font=("Calibri",20),bd=5)
heading_label.place(x=50,y=20)

enter_name = Label(window,text="Enter your name",fg="black",bg="lightcyan",font=("Calibri",15))
enter_name.place(x=30, y=92)

username = Entry(window,text="",bd=2,width=22)
username.place(x=250,y=95)

height_label = Label(window,text="Enter your height (in cm)",fg="black",bg="lightcyan",font=("Calibri",15))
height_label.place(x=30,y=150)

height_entry = Entry(window,text="",bd=2,width=22)
height_entry.place(x=250, y=155)

weight_label = Label(window,text="Enter your weight (in kg)",fg="black",bg="lightcyan",font=("Calibri",15))
weight_label.place(x=30, y=200)

weight_entry = Entry(window,text="",bd=2,width=22)
weight_entry.place(x=250, y=205)

calculate_button = Button(window,text="Calculate",fg="black",bg="cyan",bd=4,command=calculate_bmi)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result",bg="lightcyan",font=("Calibri",20))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)

result_label = Label(result_frame,text=" Your result will be displayed here ",bg="lightcyan",font=("Calibri",20),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()