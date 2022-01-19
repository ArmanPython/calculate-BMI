import tkinter as tk
from tkinter import messagebox as mess_box
from tkinter.constants import END

def bmi(bmi):
    if (bmi < 18.5):
        return "Underweight"
    elif (bmi >= 18.5 and bmi < 25):
        return "Normal weight"
    elif (bmi >= 25 and bmi < 30):
        return "Overweight"
    elif (bmi >= 30 and bmi < 35):
        return "Fat"
    elif (bmi >= 35 and bmi < 40):
        return "Very fat"
    elif (bmi >= 40):
        return " Too fat !@#$%^&* \n  erore bmi!?" 

wind = tk.Tk()
wind.title(" Calculate BMI ")
wind.config(bg="#202020")
wind.geometry("300x200")
wind.resizable(0,0)

def Calculate_BMI():
    try:
        input_Weight = float(Weight.get())
        input_Height = float(Height.get())
        User_bmi = input_Weight / (input_Height ** 2)
        Condition = bmi(User_bmi)
        mess_box.showinfo(" BMI ", f"  your bmi : {User_bmi} \n {Condition} ")
    except:
        mess_box.showerror("Error", "Height and weight should be a number")    

lbl_Weight = tk.Label(wind, text="Weight", bg="#202020", fg="white")
lbl_Weight.place(x=125, y=5)

Weight = tk.Entry(wind, bg="#4D4D4D", fg="white", font=("Arial",10), bd=0)
Weight.place(x=82, y=32)

lbl_Height = tk.Label(wind, text="Height (To meters)", bg="#202020", fg="white")
lbl_Height.place(x=125, y=50)

Height = tk.Entry(wind, bg="#4D4D4D", fg="white", font=("Arial",10), bd=0)
Height.place(x=82, y=75)

Computing_btn = tk.Button(wind, text="Computing", bg="#333333", fg="white", width=40, command=Calculate_BMI)
Computing_btn.place(x=7, y=120)

wind.mainloop()
