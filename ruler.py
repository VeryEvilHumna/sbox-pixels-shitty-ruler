"""
S&box Fnuny Pixels shitty ruler
Author: VeryEvilHuman
Version: 0.1
License: MIT
Homepage: https://github.com/VeryEvilHumna/sbox-pixels-shitty-ruler
"""


import keyboard
import pyautogui 
import customtkinter as ctk

######## Custom tkinter settings

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

######## Init window

window = ctk.CTk()
window.title("S&box Fnuny Pixels shitty ruler by VeryEvilHuman")
window.config(padx=20, pady=20)
window.geometry("750x330")
window.wm_attributes("-topmost", True)
window.resizable(False, False)

##

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window.geometry(f"+{screen_width-1000}+100")

######## Init CTk variables

mouseX = ctk.StringVar()
mouseY = ctk.StringVar()


mouseXul = ctk.IntVar()
mouseYul = ctk.IntVar()

mouseXlr = ctk.IntVar()
mouseYlr = ctk.IntVar()


mouseartYul = ctk.IntVar()
mouseartYlr = ctk.IntVar()

mouseartXul = ctk.IntVar()
mouseartXlr = ctk.IntVar()

result = ctk.StringVar(value="There will be result")
pixelcount = ctk.StringVar(value="There will be pixel count")

radio_var = ctk.IntVar(value=0)

cooldown = ctk.StringVar(value="")


####### Window closing function

def on_closing():
    quit()

window.protocol("WM_DELETE_WINDOW", on_closing)

########

################################################ Code 

######## Mouse pos realtime updating

def mouse_pos_update():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY = pyautogui.position()
    mouseX.set(f"X: {currentMouseX}")
    mouseY.set(f"Y: {currentMouseY}")
    window.after(10, mouse_pos_update)

######## Hotkeys

def hotkey_function():
    print(currentMouseX, currentMouseY)
    window.lift()

    if radio_var.get() == 1:
        mouseXul.set(currentMouseX)
        mouseYul.set(currentMouseY)
    elif radio_var.get() == 2:
        mouseXlr.set(currentMouseX)
        mouseYlr.set(currentMouseY)
    elif radio_var.get() == 3:
        mouseartXul.set(currentMouseX)
        mouseartYul.set(currentMouseY)
    elif radio_var.get() == 4:
        mouseartXlr.set(currentMouseX)
        mouseartYlr.set(currentMouseY)


keyboard.add_hotkey('ctrl + c', hotkey_function)

####### Calculate size

def solve():
    
    pixel_size = (mouseXul.get() - mouseXlr.get(),
                  mouseYul.get() - mouseYlr.get())
    
    art_size = (mouseartXul.get() - mouseartXlr.get(),
                mouseartYul.get() - mouseartYlr.get())
    
    art_true_size = (round(art_size[0] / pixel_size[0]),
                     round(art_size[1] / pixel_size[1]))

    result.set(f"{art_true_size[0]} x {art_true_size[1]}")

    if cooldownInput.get() == "":
        pixelcount.set(f"{art_true_size[0] * art_true_size[1]} pixels")

    else:
        time = ((art_true_size[0] * art_true_size[1]) * int(cooldownInput.get()))
        pixelcount.set(f"{art_true_size[0] * art_true_size[1]} pixels, at least {time/60} minutes")


########################################## Tkinter (again (I'm too lazy to rewrite this tool with classes))


####### Init CTk widgets

guideLabel = ctk.CTkLabel(window, text="Tip: 'Ctrl + C' to get cursor position", fg_color=("white","darkblue"), corner_radius=15)


mouseXLabel = ctk.CTkLabel(window, width=40, textvariable=mouseX, fg_color=("white","black"), corner_radius=15)
mouseYLabel = ctk.CTkLabel(window, width=40, textvariable=mouseY, fg_color=("white","black"), corner_radius=15)


mouseXulLabel = ctk.CTkLabel(window, textvariable=mouseXul, fg_color=("white","black"), corner_radius=15)
mouseYulLabel = ctk.CTkLabel(window, textvariable=mouseYul, fg_color=("white","black"), corner_radius=15)

mouseXlrLabel = ctk.CTkLabel(window, textvariable=mouseXlr, fg_color=("white","black"), corner_radius=15)
mouseYlrLabel = ctk.CTkLabel(window, textvariable=mouseYlr, fg_color=("white","black"), corner_radius=15)


mouseartXulLabel = ctk.CTkLabel(window, textvariable=mouseartXul, fg_color=("white","black"), corner_radius=15)
mouseartYulLabel = ctk.CTkLabel(window, textvariable=mouseartYul, fg_color=("white","black"), corner_radius=15)

mouseartXlrLabel = ctk.CTkLabel(window, textvariable=mouseartXlr, fg_color=("white","black"), corner_radius=15)
mouseartYlrLabel = ctk.CTkLabel(window, textvariable=mouseartYlr, fg_color=("white","black"), corner_radius=15)


radiobutton1 = ctk.CTkRadioButton(window, text="Step 1: Upper left corner of the pixel", variable=radio_var, value=1)
radiobutton2 = ctk.CTkRadioButton(window, text="Step 2: Lower right corner of the pixel", variable=radio_var, value=2)
radiobutton3 = ctk.CTkRadioButton(window, text="Step 3: Upper left corner of the art", variable=radio_var, value=3)
radiobutton4 = ctk.CTkRadioButton(window, text="Step 4: Lower right corner of the art", variable=radio_var, value=4)

cooldownLabel = ctk.CTkLabel(window, text="Cooldown (s):", corner_radius=15)
cooldownInput = ctk.CTkEntry(window, corner_radius=5, width=100, textvariable=cooldown)


solvebutton = ctk.CTkButton(window, text="Solve", command=solve, corner_radius=5)

resultLabel = ctk.CTkLabel(window, textvariable=result, fg_color=("white","black"), corner_radius=15)
pixelcountLabel = ctk.CTkLabel(window, textvariable=pixelcount, fg_color=("white","black"), corner_radius=15)

######### Pack widgets

mouseXLabel.grid(row=0, column=4, padx=5, pady=5)
mouseYLabel.grid(row=1, column=4, padx=5, pady=5)

radiobutton1.grid(row=0, column=2, padx=5, pady=5)
radiobutton2.grid(row=0, column=3, padx=5, pady=5)

radiobutton3.grid(row=3, column=2, padx=5, pady=5)
radiobutton4.grid(row=3, column=3, padx=5, pady=5)


mouseXulLabel.grid(row=1, column=2, padx=5, pady=5)
mouseYulLabel.grid(row=2, column=2, padx=5, pady=5)

mouseXlrLabel.grid(row=1, column=3, padx=5, pady=5)
mouseYlrLabel.grid(row=2, column=3, padx=5, pady=5)

mouseartXulLabel.grid(row=4, column=2, padx=5, pady=5)
mouseartYulLabel.grid(row=5, column=2, padx=5, pady=5)

mouseartXlrLabel.grid(row=4, column=3, padx=5, pady=5)
mouseartYlrLabel.grid(row=5, column=3, padx=5, pady=5)


cooldownLabel.grid(row=3, column=4, padx=5, pady=5)
cooldownInput.grid(row=4, column=4, padx=5, pady=5)

solvebutton.grid(row=5, column=4)

resultLabel.grid(row=6, column=4, padx=5, pady=5)
pixelcountLabel.grid(row=7, column=4, padx=5, pady=5)

guideLabel.grid(row=6, column=0, columnspan=4, padx=5, pady=5)




######### Entry point

if __name__ == "__main__":
    mouse_pos_update()
    window.mainloop()