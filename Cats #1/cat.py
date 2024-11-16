from abstracts import Animal, Pet

class Cat(Animal, Pet):
    species = "Felis catus"
    total_cats = 0  # Класс-атрибут для отслеживания общего числа кошек

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._hunger = 0
        Cat.total_cats += 1
        print(f"Создана кошка: {self.name}")

    @property
    def name(self) -> str:
        """Получение имени кошки"""
        return self._name

    @name.setter
    def name(self, value: str):
        """Установка имени кошки"""
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value

    @property
    def age(self) -> int:
        """Получение возраста кошки"""
        return self._age

    @age.setter
    def age(self, value: int):
        """Установка возраста кошки"""
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    def make_sound(self):
        """Реализация абстрактного метода для звука кошки"""
        return "Мяу!"

    def move(self):
        """Реализация абстрактного метода для передвижения кошки"""
        return "Кошка двигается грациозно."

    def feed(self, amount: int):
        """Метод для кормления кошки"""
        self._hunger -= amount
        if self._hunger < 0:
            self._hunger = 0
        print(f"{self.name} накормлена. Уровень голода: {self._hunger}")

    def play(self, time: int):
        """Реализация абстрактного метода для игры с кошкой"""
        self._hunger += time
        print(f"{self.name} поиграла. Уровень голода: {self._hunger}")

    @staticmethod
    def is_domesticated() -> bool:
        """Статический метод для проверки прирученности"""
        return True

    @classmethod
    def species_info(cls) -> str:
        """Метод класса для получения информации о виде"""
        return f"Вид: {cls.species}"

    @classmethod
    def get_total_cats(cls) -> int:
        """Метод класса для получения общего числа кошек"""
        return cls.total_cats

    def __str__(self):
        return f"Кошка по имени {self.name}, возраст: {self.age} лет."

    def __repr__(self):
        return f"Cat(name={self.name!r}, age={self.age!r})"

    def __del__(self):
        """Деструктор класса Cat"""
        Cat.total_cats -= 1
        print(f"Кошка {self.name} удалена. Осталось кошек: {Cat.total_cats}")

    # Пример контекстного менеджера
    def __enter__(self):
        print(f"{self.name} готова к использованию в контекстном менеджере.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} завершила работу в контекстном менеджере.")
        # Можно добавить обработку исключений, если необходимо

    # Пример метода экземпляра
    def rename(self, new_name: str):
        """Метод для изменения имени кошки"""
        self.name = new_name
        print(f"Кошка переименована в {self.name}")

    # Пример метода с декоратором
    @property
    def is_hungry(self) -> bool:
        """Свойство, определяющее, голодна ли кошка"""
        return self._hunger > 5

    # Методы можно продолжать расширять, добавляя дополнительные функциональные возможности
    # Например:
    # def sleep(self, hours: int):
    #     """Метод для сна кошки"""
    #     pass 