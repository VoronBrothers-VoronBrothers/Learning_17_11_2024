import tkinter as tk
from tkinter import messagebox
from database import Database

class App:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Запись данных")
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.save_button = tk.Button(root, text="Сохранить", command=self.save_record)
        self.save_button.pack(pady=5)
        
    def save_record(self):
        text = self.entry.get()
        if text:
            self.db.insert_record(text)
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Успех", "Запись сохранена!")
        else:
            messagebox.showwarning("Предупреждение", "Поле ввода не может быть пустым.")
            
    def on_closing(self):
        self.db.close()
        self.root.destroy() 