import tkinter as tk

fenster = tk.Tk()
fenster.geometry("200x100")
label = tk.Label(fenster, text="Hallo Welt!")
label.pack()

def befehl():
    fenster.destroy()

button = tk.Button(fenster, text="OK", command=befehl)
button.pack()
