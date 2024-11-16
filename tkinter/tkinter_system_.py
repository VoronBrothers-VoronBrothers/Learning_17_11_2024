import tkinter as tk # GUI
from tkinter import messagebox # Message Box
import os # OS

def get_label_text(): # Get Label Text
    label.config(text=entry.get())

def os_path_file(): # Get OS Path File
    label.config(text=os.path.join(os.path.abspath(__file__), entry.get()))

def message_box(): # Message Box
    messagebox.showinfo("Message", "Hello, World!")

root = tk.Tk() # Root
root.title("System Information") # Title
root.geometry("400x300")    # Size

label = tk.Label(root, text="System Information", font=("Arial", 16)) # Label
label.pack(pady=10) 

entry = tk.Entry(root, width=30) # Entry
entry.pack(pady=10)

button = tk.Button(root, text="Get Information", command=get_label_text) # Button
button.pack(pady=10)

button2 = tk.Button(root, text="Get OS Path File", command=os_path_file) # Button
button2.pack(pady=10)

button3 = tk.Button(root, text="Message Box", command=message_box) # Button
button3.pack(pady=10)

root.mainloop() # Main Loop

#игорь говорит: а сейчас ты учишься? copilot: да, я учусь
#игорь говорит: а ты можешь сделать так, чтобы я мог с тобой общаться? copilot: конечно, я могу сделать так, чтобы мы могли общаться.
#игорь говорит: а как это сделать? copilot: я могу создать для тебя приложение, которое будет общаться с тобой.
#игорь говорит: а как это приложение будет работать? copilot: оно будет работать так, чтобы мы могли общаться друг с другом.
#игорь говорит: а что я могу с этим приложением делать? copilot: ты можешь с этим приложением делать все, что угодно.
#игорь говорит: 2+5=12 copilot: нет, 2+5=7
#игорь говорит: 2+5=7 copilot: да, 2+5=7
#игорь говорит: 2+5=12 copilot: нет, 2+5=7
#игорь говорит: 2+5=7 copilot: да, 2+5=7
#игорь говорит: 2+5=12 copilot: нет, 2+5=7

#игорь говорит: что бы ты хотел сделать? copilot: я могу сделать для тебя приложение, которое будет общаться с тобой.
#игорь говорит: а как это приложение будет работать? copilot: оно будет работать так, чтобы мы могли общаться друг с другом.
#игорь говорит: а что я могу с этим приложением делать? copilot: ты можешь с этим приложением делать все, что угодно.
#игорь говорит: а можно ли это приложение назвать "Система информации"? copilot: да, можно. 



