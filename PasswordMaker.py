import random
import string
import tkinter as tk

root = tk.Tk()
root.title("Password Maker")
root.geometry("300x300")


def password_maker():
    global app
    app = app_web.get()
    root.destroy()

    window = tk.Tk()
    window.title("Password Maker")
    window.geometry("300x300")

    def btn_confirm():

        try:
            length = int(entry.get())
        except (ValueError):
            result["text"] = "Enter a number"
        if capital.get() == 1:
            capletters = list(string.ascii_uppercase)
        else:
            capletters = []
        if lowercase.get() == 1:
            lowletters = list(string.ascii_lowercase)
        else:
            lowletters = []
        if number.get() == 1:
            numbers = list(string.digits)
        else:
            numbers = []
        if special_characters.get() == 1:
            special = list(string.punctuation)
        else:
            special = []
        all_characters = capletters + lowletters + numbers + special
        password = "".join(random.choices(all_characters, k=length))
        result["text"] = password
        with open("Passwords", "a") as passwords:
            for x in range(1):
                passwords.write(f"{app} = {password}")
            for x in range(1):
                passwords.write("\n")

    text = tk.Label(
        master=window, text="Enter the length of the password:", width=40)
    text.grid(row=0, column=0)

    entry = tk.Entry(master=window)
    entry.grid(row=1, column=0)

    confirm = tk.Button(master=window, text="Confirm", command=btn_confirm)
    confirm.grid(row=2, column=0)

    result = tk.Label(master=window, text="")
    result.grid(row=4, column=0)

    capital = tk.IntVar()
    upper_check = tk.Checkbutton(
        master=window, variable=capital, text="Uppercase")
    upper_check.grid(row=5, column=0)

    lowercase = tk.IntVar()
    lower_check = tk.Checkbutton(
        master=window, variable=lowercase, text="Lowercase")
    lower_check.grid(row=6, column=0)

    number = tk.IntVar()
    number_check = tk.Checkbutton(
        master=window, variable=number, text="Numbers")
    number_check.grid(row=7, column=0)

    special_characters = tk.IntVar()
    special_check = tk.Checkbutton(
        master=window, variable=special_characters, text="Special characters")
    special_check.grid(row=8, column=0)

    window.mainloop()


message = tk.Label(master=root, text="Enter the name of the app/website")
message.pack()

app_web = tk.Entry(master=root)
app_web.pack()

finish = tk.Button(master=root, text="Finish", command=password_maker)
finish.pack()

root.mainloop()
