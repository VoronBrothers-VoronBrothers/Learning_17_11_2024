import os # Модуль для работы с файловой системой

def list_dir(path=r"C:\Users\VoronBrothers\Downloads"):
    try:
        # Получаем список элементов в указанной директории
        elements_in_dir = os.listdir(path)
        list_of_files = []
        for element in elements_in_dir:
            # Создаём полный путь к элементу
            full_path = os.path.join(path, element)
            # Проверяем, является ли элемент файлом
            is_file = os.path.isfile(full_path)
            # Добавляем информацию о элементе в список
            list_of_files.append(f"{element} - {is_file}")
        return list_of_files
    except FileNotFoundError as e:
        # Выводим сообщение об ошибке, если директория не найдена
        print(f"File not found: {e}")

if __name__ == "__main__":
    # Выводим отсортированный список файлов и папок
    print(sorted(list_dir()))
