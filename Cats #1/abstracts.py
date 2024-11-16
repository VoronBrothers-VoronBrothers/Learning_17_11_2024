from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Метод для издания звука животного"""
        pass

    @abstractmethod
    def move(self):
        """Метод для передвижения животного"""
        pass

class Pet(ABC):
    @abstractmethod
    def play(self, time: int):
        """Метод для игры с питомцем"""
        pass 