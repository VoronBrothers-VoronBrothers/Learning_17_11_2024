import os

print(os.name)

print(f"os.path.dirname(os.path.abspath(__file__)): {os.path.dirname(os.path.abspath(__file__))}") # текущая директория
print(f"os.path.basename(os.path.abspath(__file__)): {os.path.basename(os.path.abspath(__file__))}") # имя файла
