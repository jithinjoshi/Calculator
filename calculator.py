from tkinter import *


cal = Tk()
cal.title("Calculator")
cal.configure(bg="#45676b")
e = Entry(cal, width=60, borderwidth=5, justify="right", border=15, bg="#888894",cursor="None")
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    global s_num
    s_num = int(second_number)
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + s_num)

    if math == "subtraction":
        e.insert(0, f_num - s_num)

    if math == "multiplication":
        e.insert(0, f_num * s_num)

    if math == "division":
        e.insert(0, f_num / s_num)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



# Define Buttons
button1 = Button(cal, text="1", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(1))
button2 = Button(cal, text="2", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(2))
button3 = Button(cal, text="3", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(3))
button4 = Button(cal, text="4", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(4))
button5 = Button(cal, text="5", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(5))
button6 = Button(cal, text="6", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(6))
button7 = Button(cal, text="7", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(7))
button8 = Button(cal, text="8", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(8))
button9 = Button(cal, text="9", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(9))
button0 = Button(cal, text="0", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                 command=lambda: button_click(0))
button_add = Button(cal, text="+", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                    command=button_add)
button_sub = Button(cal, text="-", padx=42, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                    command=button_sub)
button_mul = Button(cal, text="x", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                    command=button_mul)
button_div = Button(cal, text="/", padx=42, pady=20, fg="black", font=("arial", 13, "bold"), activebackground="#e3e01e",
                    command=button_div)
button_equal = Button(cal, text="=", padx=40, pady=20, fg="black", font=("arial", 13, "bold"),
                      activebackground="#e3e01e", command=button_equal)
button_clear = Button(cal, text="C", padx=40, pady=20, fg="black", font=("arial", 13, "bold"), bg="red",
                      activebackground="#e3e01e", command=button_clear)


# put buttons in to the screen

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button_div.grid(row=4, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button0.grid(row=5, column=0)
button_equal.grid(row=5, column=1)
button_add.grid(row=5, column=2)

button_clear.grid(row=5, column=3)


cal.mainloop()
