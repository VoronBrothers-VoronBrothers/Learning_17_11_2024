import tkinter as tk #tkinter is a GUI library for python
from tkinter import ttk #ttk is a theme of tkinter
from tkinter import messagebox #messagebox is a library for showing messages
root = tk.Tk() #root is a window
root.title("VoronBrothers Notebook") #title of the window
root.geometry("600x400") #size of the window

#def save text from entry to a file and save previous text to the file
def save_text():
    try:
        with open("text.txt", "a") as file:
            file.write(entry.get()+"\n")
            entry.delete(0, tk.END)
            #messagebox.showinfo("Success", "Text saved successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)

#def clear file with accept messagebox
def clear_file():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear the file?"):
        with open("text.txt", "w") as file:
            file.write("")

#about page
def about_page():
    messagebox.showinfo("About", "Company Name: VoronBrothers Company\nVersion: 1.0\nAuthor: VoronBrothers")

# Create a Notebook widget
notebook = ttk.Notebook(root)

# Add pages to the Notebook
page1 = tk.Frame(notebook)
page2 = tk.Frame(notebook)

notebook.add(page1, text="Страница 1") #add page1 to the notebook
notebook.add(page2, text="Страница 2") #add page2 to the notebook

notebook.pack(expand=True, fill="both") #pack the notebook

#add a entry to the page
entry = tk.Entry(page1)
entry.config(width=50, font=("Arial", 16), justify="center", insertbackground="black")
#entry.insert(0, "Enter text here") #insert text to the entry
entry.pack(pady=10)

#add a button to the page
button = tk.Button(page1, text="Save", command=save_text)
button.pack(pady=10)

#add a button to the page
button = tk.Button(page1, text="Clear", command=clear_file)
button.pack(pady=10)

#add a button to the page
button = tk.Button(page1, text="About", command=about_page)
button.pack(pady=10)

root.mainloop() #run the window

