import tkinter as tk

window = tk.Tk()
window.title("Calculator")


for i in range(4):
    window.columnconfigure(i, weight=1, minsize=10)
    window.rowconfigure(i, weight=1, minsize=10)


def btn_1():
    value = inputs["text"]
    inputs["text"] = value + "1"


def btn_2():
    value = inputs["text"]
    inputs["text"] = value + "2"


def btn_3():
    value = inputs["text"]
    inputs["text"] = value + "3"


def btn_4():
    value = inputs["text"]
    inputs["text"] = value + "4"


def btn_5():
    value = inputs["text"]
    inputs["text"] = value + "5"


def btn_6():
    value = inputs["text"]
    inputs["text"] = value + "6"


def btn_7():
    value = inputs["text"]
    inputs["text"] = value + "7"


def btn_8():
    value = inputs["text"]
    inputs["text"] = value + "8"


def btn_9():
    value = inputs["text"]
    inputs["text"] = value + "9"


def btn_plus():
    value = inputs["text"]
    inputs["text"] = value + "+"


def btn_sub():
    value = inputs["text"]
    inputs["text"] = value + "-"


def btn_div():
    value = inputs["text"]
    inputs["text"] = value + "/"


def btn_multiply():
    value = inputs["text"]
    inputs["text"] = value + "*"


def btn_equal():
    try:
        value = inputs["text"]
        inputs["text"] = str(eval(value))
        history = inputs["text"]
        historylabel["text"] = f"History:\n{history}"
    except SyntaxError:
        inputs["text"] = "Enter a vaild formula"
        global okay
        okay = tk.Button(text="OKAY", height=1, width=5, command=btn_okay)
        okay.grid(column=3, row=0)


def btn_clear():
    if inputs["text"] == "":
        inputs["text"] = "No numbers available to erase"
        global okay
        okay = tk.Button(text="OKAY", height=1, width=5, command=btn_okay)
        okay.grid(column=3, row=0)
    else:
        inputs["text"] = ""


def btn_dot():
    value = inputs["text"]
    inputs["text"] = value + "."


def btn_0():
    inputs["text"] += "0"


def btn_okay():
    inputs["text"] = ""
    okay.destroy()


def btn_backspace():
    try:
        temporary_holder = ""
        value = inputs["text"]
        list_inputs = list(value)
        list_inputs.pop(-1)
        for i in list_inputs:
            temporary_holder = temporary_holder + str(i)

        inputs["text"] = temporary_holder
    except IndexError:
        inputs["text"] = "No numbers available to erase"
        global okay
        okay = tk.Button(text="OKAY", height=1, width=5, command=btn_okay)
        okay.grid(column=3, row=0)


frame = tk.Frame(width=23, height=10)
frame.grid(row=0, column=1)

inputs = tk.Label(master=frame, width=23, height=10, text="")
inputs.pack()

num1 = tk.Button(text="1", width=23, height=3, command=btn_1)
num1.grid(column=0, row=1)

num2 = tk.Button(text="2", width=23, height=3, command=btn_2)
num2.grid(column=1, row=1)

num3 = tk.Button(text="3", width=23, height=3, command=btn_3)
num3.grid(column=2, row=1)

num4 = tk.Button(text="4", width=23, height=3, command=btn_4)
num4.grid(column=0, row=2)

num5 = tk.Button(text="5", width=23, height=3, command=btn_5)
num5.grid(column=1, row=2)

num6 = tk.Button(text="6", width=23, height=3, command=btn_6)
num6.grid(column=2, row=2)

num7 = tk.Button(text="7", width=23, height=3, command=btn_7)
num7.grid(column=0, row=3)

num8 = tk.Button(text="8", width=23, height=3, command=btn_8)
num8.grid(column=1, row=3)

num9 = tk.Button(text="9", width=23, height=3, command=btn_9)
num9.grid(column=2, row=3)

plus = tk.Button(text="+", width=23, height=3, command=btn_plus)
plus.grid(column=0, row=4)

subtract = tk.Button(text="-", width=23, height=3, command=btn_sub)
subtract.grid(column=3, row=3)

multiply = tk.Button(text="*", width=23, height=3, command=btn_multiply)
multiply.grid(column=2, row=4)

equal = tk.Button(text="=", width=23, height=3, command=btn_equal)
equal.grid(column=3, row=1)

divide = tk.Button(text="/", width=23, height=3, command=btn_div)
divide.grid(column=3, row=2)

clear = tk.Button(text="Clear", width=23, height=3, command=btn_clear)
clear.grid(column=0, row=5)

dot = tk.Button(text=".", width=23, height=3, command=btn_dot)
dot.grid(column=3, row=4)

num_0 = tk.Button(text="0", width=23, height=3, command=btn_0)
num_0.grid(column=1, row=4)

backspace = tk.Button(text="Backspace", width=23,
                      height=3, command=btn_backspace)
backspace.grid(column=1, row=5)

frame1 = tk.Frame()
frame1.grid(column=0, row=0, sticky='ne')

historylabel = tk.Label(master=frame1, text="", width=23, height=2)
historylabel.pack()


window.mainloop()
