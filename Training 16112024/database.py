import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="records.db"):
        """
        Инициализирует соединение с базой данных SQLite и создает таблицу, если она не существует.

        :param db_name: Имя файла базы данных.
        """
        self.connection = sqlite3.connect(db_name)  # Устанавливаем соединение с базой данных
        self.cursor = self.connection.cursor()        # Создаем курсор для выполнения запросов
        self.create_table()                          # Создаем таблицу, если она не существует

    def create_table(self):
        """
        Создает таблицу 'records' в базе данных, если она еще не существует.
        Таблица содержит три поля: id, text и timestamp.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)                                         # Выполняем SQL-запрос для создания таблицы
        self.connection.commit()                      # Сохраняем изменения в базе данных

    def insert_record(self, text):
        """
        Вставляет новую запись в таблицу 'records' с заданным текстом и текущей датой и временем.

        :param text: Текст записи для сохранения.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущую дату и время в формате строк
        self.cursor.execute("INSERT INTO records (text, timestamp) VALUES (?, ?)", (text, timestamp))  # Вставляем запись
        self.connection.commit()                                       # Сохраняем изменения в базе данных

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.connection.close()  # Закрываем соединение с базой данных