import time
import pyautogui
import tkinter as tk


window = tk.Tk()
window.geometry("450x450")
window.title("Autoclicker")


def btn_confirm():
    try:
        click_speed = confirm.get()
        if click_speed == options[0]:
            countdown = 10
            seconds = int(entry.get())
            for x in range(countdown):
                window.update()
                countdown_label["text"] = f"The program starts in {countdown} seconds"
                time.sleep(1)
                countdown -= 1

            start = time.time()
            while True:
                pyautogui.PAUSE = 0.09
                pyautogui.click()
                current = time.time()
                elapsed = current - start
                window.update()
                if elapsed >= seconds:
                    countdown_label["text"] = f"Finished iteration in {int(elapsed)} seconds"
                    break
        elif click_speed == options[1]:
            countdown = 10
            seconds = int(entry.get())
            for x in range(countdown):
                window.update()
                countdown_label["text"] = f"The program starts in {countdown} seconds"
                time.sleep(1)
                countdown -= 1

            start = time.time()
            while True:
                pyautogui.PAUSE = 0.041
                pyautogui.click()
                current = time.time()
                elapsed = current - start
                window.update()
                if elapsed >= seconds:
                    countdown_label["text"] = f"Finished iteration in {int(elapsed)} seconds"
                    break
        elif click_speed == options[2]:
            countdown = 10
            seconds = int(entry.get())
            for x in range(countdown):
                window.update()
                countdown_label["text"] = f"The program starts in {countdown} seconds"
                time.sleep(1)
                countdown -= 1

            start = time.time()
            while True:
                pyautogui.PAUSE = 0.025
                pyautogui.click()
                current = time.time()
                elapsed = current - start
                window.update()
                if elapsed >= seconds:
                    countdown_label["text"] = f"Finished iteration in {int(elapsed)} seconds"
                    break
        elif click_speed == options[3]:
            countdown = 10
            seconds = int(entry.get())
            for x in range(countdown):
                window.update()
                countdown_label["text"] = f"The program starts in {countdown} seconds"
                time.sleep(1)
                countdown -= 1

            start = time.time()
            while True:
                pyautogui.PAUSE = 0.013
                pyautogui.click()
                current = time.time()
                elapsed = current - start
                window.update()
                if elapsed >= seconds:
                    countdown_label["text"] = f"Finished iteration in {int(elapsed)} seconds"
                    break
        else:
            countdown = 10
            seconds = int(entry.get())
            for x in range(countdown):
                window.update()
                countdown_label["text"] = f"The program starts in {countdown} seconds"
                time.sleep(1)
                countdown -= 1

            start = time.time()
            while True:
                pyautogui.PAUSE = 0.0006
                pyautogui.click()
                current = time.time()
                elapsed = current - start
                window.update()
                if elapsed >= seconds:
                    countdown_label["text"] = f"Finished iteration in {int(elapsed)} seconds"
                    break
    except ValueError:
        countdown_label["text"] = "Enter the amount of seconds"


label = tk.Label(
    master=window, text="Enter the seconds and speed:", width=30)
label.grid(row=0, column=0)

entry = tk.Entry(width=30)
entry.grid(row=1, column=0)

button = tk.Button(master=window, text="Confirm", command=btn_confirm)
button.grid(row=2, column=0)

options = [
    "10 CPS",
    "20 CPS",
    "30 CPS",
    "50 CPS",
    "60 CPS",


]
confirm = tk.StringVar()
confirm.set(options[0])

list = tk.OptionMenu(window, confirm, *options)
list.grid(row=1, column=1)

countdown_label = tk.Label(master=window, text="")
countdown_label.grid()

window.mainloop()
