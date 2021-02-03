import tkinter as tk
from tkinter import*

def btnClick(numbers):
    textDisplay.insert("end", (numbers))

def btnAdd():
    fnum = textDisplay.get()
    global firstNumber
    global math
    math = "addition"
    
    try:
        if fnum != "":
            if float(fnum) - int(fnum) == int(fnum) - int(fnum):
                firstNumber = int(fnum)
        else:
            pass
    except Exception as e:
        firstNumber = float(fnum)

    textDisplay.delete(0, "end")
    textDisplay2.delete(0, "end")
    textDisplay2.insert("end", f'{firstNumber} + ')

def btnSub():
    fnum = textDisplay.get()
    global firstNumber
    global math
    math = "subtraction"

    try:
        if fnum != "":
            if float(fnum) - int(fnum) == int(fnum) - int(fnum):
                firstNumber = int(fnum)
        else:
            pass
    except Exception as e:
        firstNumber = float(fnum)

    textDisplay.delete(0, "end")
    textDisplay2.delete(0, "end")
    textDisplay2.insert("end", f'{firstNumber} - ')

def btnMulitply():
    fnum = textDisplay.get()
    global firstNumber
    global math
    math = "multiplication"
    
    try:
        if fnum != "":
            if float(fnum) - int(fnum) == int(fnum) - int(fnum):
                firstNumber = int(fnum)
        else:
            pass
    except Exception as e:
        firstNumber = float(fnum)

    textDisplay.delete(0, "end")
    textDisplay2.delete(0, "end")
    textDisplay2.insert("end", f'{firstNumber} * ')

def btnDiv():
    fnum = textDisplay.get()
    global firstNumber
    global math
    math = "division"
    
    try:
        if fnum != "":
            if float(fnum) - int(fnum) == int(fnum) - int(fnum):
                firstNumber = int(fnum)
        else:
            pass
    except Exception as e:
        firstNumber = float(fnum)

    textDisplay.delete(0, "end")
    textDisplay2.delete(0, "end")
    textDisplay2.insert("end", f'{firstNumber} / ')

def btnPercent():
    num = textDisplay.get()
    global Number
    textDisplay.delete(0, "end")

    try:
        if num != "":
            if float(num) - int(num) == int(num) - int(num):
                Number = int(num)
        else:
            pass
    except Exception as e:
        Number = float(num)

    if Number == "":
        pass
    elif Number != "":
        Number = ((Number)/100)
        textDisplay.insert("end", Number)
        textDisplay2.delete(0, "end")
        textDisplay2.insert("end", f'{Number} %')

def btnPlus_Minus():
    num = textDisplay.get()
    global Number
    
    try:
        if num != "":
            if float(num) - int(num) == int(num) - int(num):
                Number = int(num)
        else:
            pass
    except Exception as e:
        Number = float(num)

    textDisplay.delete(0, "end")
    if Number == "":
        pass
    elif Number != "":
        Number = ((Number) * -1)
        textDisplay.insert("end", Number)

def  btnBackspace():
    num = textDisplay.get()
    global Number
    Number = str(num)
    textDisplay.delete(0, "end")
    if Number == "":
        pass
    elif Number != "":
        Number = Number[:-1]

        textDisplay.insert("end", Number)

def btnPoint():
    try:
        if textDisplay.get() == "":
            pass
        else:
            num = textDisplay.get()
            global Number
            Number = (num)
            if type(Number) != float():
                textDisplay.delete(0, "end")
                Number = float(num)
                Number = str(Number)
                Number = Number[:-1]
                textDisplay.insert("end", Number)
            else:
                pass
    except Exception as e:
        raise e

def btnEquals():
    snum = textDisplay.get()
    global secondNumber

    try:
        if snum != "":
            if float(snum) - int(snum) == int(snum) - int(snum):
                secondNumber = int(snum)
        else:
            pass
    except Exception as e:
        secondNumber = float(snum)

    if firstNumber or secondNumber == int():
        if math == "addition":
            total = ((firstNumber) + (secondNumber))
            textDisplay.delete(0, "end")
            textDisplay.insert("end", total)
            textDisplay2.delete(0, "end") 
            text2 = f'{firstNumber} + {secondNumber}'
            textDisplay2.insert("end", text2)

        elif math == "subtraction":
            total = ((firstNumber) - (secondNumber))
            textDisplay.delete(0, "end")
            text2 = f'{firstNumber} - {secondNumber}'
            textDisplay2.delete(0, "end")
            textDisplay2.insert("end", text2)
            textDisplay.insert("end", total)

        elif math == "multiplication":
            total = ((firstNumber) * (secondNumber))
            textDisplay.delete(0, "end")
            textDisplay.insert("end", total)
            textDisplay2.delete(0, "end")
            text2 = f'{firstNumber} * {secondNumber}'
            textDisplay2.insert("end", text2)

        elif math == "division":
            total = ((firstNumber) / (secondNumber))
            textDisplay.delete(0, "end")
            textDisplay.insert("end", total) 
            textDisplay2.delete(0, "end")
            text2 = f'{firstNumber} / {secondNumber}'
            textDisplay2.insert("end", text2)  


def btnClear():
    textDisplay.delete(0, "end")

cal = tk.Tk()
cal.title("Calculator")
cal.resizable(False, False)
cal.configure(background = '#30304B')

cal.geometry("400x700")

textDisplay = tk.Entry(cal, font = ('arial', 40, 'bold'), borderwidth = 0, bg = "#30304B", fg = "#FFFFFF", justify = 'right')
textDisplay.place(x = 20, y = 46, width = 360, height = 92)

textDisplay2 = tk.Entry(cal, font = ('arial', 20, 'bold'), borderwidth = 0, bg = "#30304B", fg = "#676767", justify = 'right')
textDisplay2.place(x = 20, y = 138, width = 360, height = 46)

Icon_img = PhotoImage(file = 'Images/Icon.png')
cal.iconphoto(False, Icon_img)

Clear_btn_img = PhotoImage(file = 'Images/Clear-btn.png')
Plus_Minus_btn_img = PhotoImage(file = 'Images/Plus_Minus-btn.png')
Percent_btn_img = PhotoImage(file = 'Images/Percent-btn.png')
Div_btn_img = PhotoImage(file = 'Images/Div-btn.png')

Seven_btn_img = PhotoImage(file = 'Images/Seven-btn.png')
Eight_btn_img = PhotoImage(file = 'Images/Eight-btn.png')
Nine_btn_img = PhotoImage(file = 'Images/Nine-btn.png')
Multiply_btn_img = PhotoImage(file = 'Images/Multiply-btn.png')

Four_btn_img = PhotoImage(file = 'Images/Four-btn.png')
Five_btn_img = PhotoImage(file = 'Images/Five-btn.png')
Six_btn_img = PhotoImage(file = 'Images/Six-btn.png')
Subtract_btn_img = PhotoImage(file = 'Images/Subtract-btn.png')

One_btn_img = PhotoImage(file = 'Images/One-btn.png')
Two_btn_img = PhotoImage(file = 'Images/Two-btn.png')
Three_btn_img = PhotoImage(file = 'Images/Three-btn.png')
Add_btn_img = PhotoImage(file = 'Images/Add-btn.png')

Zero_btn_img = PhotoImage(file = 'Images/Zero-btn.png')
Point_btn_img = PhotoImage(file = 'Images/Point-btn.png')
Backspace_btn_img = PhotoImage(file = 'Images/Backspace-btn.png')
Equals_btn_img = PhotoImage(file = 'Images/Equals-btn.png')

#row 1 
Clear_btn = tk.Button(cal, image = Clear_btn_img, borderwidth = 0, bg = "#30304B", command = btnClear)
Clear_btn.place(x = 24, y = 232, width = 76, height = 76)

Plus_Minus_btn = tk.Button(cal, image = Plus_Minus_btn_img, borderwidth = 0, bg = "#30304B", command = btnPlus_Minus)
Plus_Minus_btn.place(x = 116, y = 232, width = 76, height = 76)

Percent_btn = tk.Button(cal, image = Percent_btn_img, borderwidth = 0, bg = "#30304B", command = btnPercent)
Percent_btn.place(x = 208, y = 232, width = 76, height = 76)

Div_btn = tk.Button(cal, image = Div_btn_img, borderwidth = 0, bg = "#30304B", command = btnDiv)
Div_btn.place(x = 300, y = 232, width = 76, height = 76)

#row 2
Seven_btn = tk.Button(cal, image = Seven_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(7))
Seven_btn.place(x = 24, y = 324, width = 76, height = 76)

Eight_btn = tk.Button(cal, image = Eight_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(8))
Eight_btn.place(x = 116, y = 324, width = 76, height = 76)

Nine_btn = tk.Button(cal, image = Nine_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(9))
Nine_btn.place(x = 208, y = 324, width = 76, height = 76)

Multiply_btn = tk.Button(cal, image = Multiply_btn_img, borderwidth = 0, bg = "#30304B", command = btnMulitply)
Multiply_btn.place(x = 300, y = 324, width = 76, height = 76)

#row 3
Four_btn = tk.Button(cal, image = Four_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(4))
Four_btn.place(x = 24, y = 416, width = 76, height = 76)

Five_btn = tk.Button(cal, image = Five_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(5))
Five_btn.place(x = 116, y = 416, width = 76, height = 76)

Six_btn = tk.Button(cal, image = Six_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(6))
Six_btn.place(x = 208, y = 416, width = 76, height = 76)

Subtract_btn = tk.Button(cal, image = Subtract_btn_img, borderwidth = 0, bg = "#30304B", command = btnSub)
Subtract_btn.place(x = 300, y = 416, width = 76, height = 76)

#row 4
One_btn = tk.Button(cal, image = One_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(1))
One_btn.place(x = 24, y = 508, width = 76, height = 76)

Two_btn = tk.Button(cal, image = Two_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(2))
Two_btn.place(x = 116, y = 508, width = 76, height = 76)

Three_btn = tk.Button(cal, image = Three_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(3))
Three_btn.place(x = 208, y = 508, width = 76, height = 76)

Add_btn = tk.Button(cal, image = Add_btn_img, borderwidth = 0, bg = "#30304B", command = btnAdd)
Add_btn.place(x = 300, y = 508, width = 76, height = 76)

#row 5
Zero_btn = tk.Button(cal, image = Zero_btn_img, borderwidth = 0, bg = "#30304B", command = lambda: btnClick(0))
Zero_btn.place(x = 24, y = 600, width = 76, height = 76)

Point_btn = tk.Button(cal, image = Point_btn_img, borderwidth = 0, bg = "#30304B", command = btnPoint)
Point_btn.place(x = 116, y = 600, width = 76, height = 76)

Backspace_btn = tk.Button(cal, image = Backspace_btn_img, borderwidth = 0, bg = "#30304B", command = btnBackspace)
Backspace_btn.place(x = 208, y = 600, width = 76, height = 76)

Equals_btn = tk.Button(cal, image = Equals_btn_img, borderwidth = 0, bg = "#30304B", command = btnEquals)
Equals_btn.place(x = 300, y = 600, width = 76, height = 76)

cal.mainloop()