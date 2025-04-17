from tkinter import *

PIN = 7007 # This is the correct PIN




user_input = []
attempts = 3

def alarm():
    for row in button_refs:
        for btn in row:
            btn.config(state=DISABLED)
    info_label.config(text="Too many wrong attempts!", fg="#df3232")
    input("Alarm! Keypad is locked, press any key to unlock it!")
    for row in button_refs:
        for btn in row:
            btn.config(state=NORMAL)
    reset()

def check_input(input):
    if input == PIN:
        return True
    else:
        return False

def process_input(value):
    if value == "ENT":
        enter()
    elif value == "DEL":
        if user_input != []:
            user_input.pop()
            update()
    else:
        user_input.append(value)
        update()

def enter():
    global attempts
    if attempts > 0:
        if user_input != []:
            if check_input(int(''.join(map(str, user_input)))):
                user_input.clear()
                info_label.config(text="Opening...", fg="#168116")
                input("Door is open! Press any key to close!")
                reset()
            else:
                user_input.clear()
                info_label.config(text="Incorrect PIN!", fg="#df3232")
                attempts -= 1
        else:
            pass
    else:
        alarm()
        attempts = 3

def update():
    info_label.config(text=user_input, fg="#000000")

def reset():
    info_label.config(text="Welcome! Please enter PIN to continue!", fg="#000000")






root = Tk()
root.geometry("600x525")
root.config(bg="#c5e3e7")
root.resizable(False, False)
root.title("Access Control")

info_frame = Frame(bg="#f0f0f0", height=100)
info_frame.pack(fill=X, pady=30, padx=30)

info_label = Label(info_frame, font=("TkDefaultFont", 20), text="Welcome! Please enter PIN to continue!")
info_label.pack(pady=30, padx=30)

input_frame = Frame(bg="#f0f0f0", height=600)
input_frame.pack(fill=X, padx=30, pady=30)

button_frame = Frame(input_frame, bg="#f0f0f0")
button_frame.pack(anchor="center")

button_refs = []

buttons = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["0", "ENT", "DEL"]
]

for r, row in enumerate(buttons):
    row_buttons = []
    for c, val in enumerate(row):

        bg_color = "#ffffff"

        if val == "ENT":
            bg_color = "#90ee90"
            font=("TkDefaultFont", 18, "bold")
        elif val == "DEL":
            bg_color = "#ff7f7f"

        btn = Button(button_frame, font=("TkDefaultFont", 18),text=val, width=12, height=2, relief=FLAT, bg=bg_color, command=lambda v=val: process_input(v))
        btn.grid(row=r, column=c, pady=1, padx=1)
        row_buttons.append(btn)
    
    button_refs.append(row_buttons)

root.mainloop()