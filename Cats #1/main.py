from cat import Cat

def main():
    with Cat(name="Мурка", age=3) as my_cat:
        print(my_cat)
        print(my_cat.make_sound())
        print(my_cat.move())
        my_cat.play(2)
        my_cat.feed(1)
        print(Cat.is_domesticated())
        print(Cat.species_info())
        print(f"Всего кошек: {Cat.get_total_cats()}")
        print(f"Голодна ли {my_cat.name}? {'Да' if my_cat.is_hungry else 'Нет'}")
        my_cat.rename("Барсик")
        # my_cat.sleep(5)  # Пример дополнительного метода, закомментированного для демонстрации

    print(f"Всего кошек после выхода из контекста: {Cat.get_total_cats()}")

if __name__ == "__main__":
    main() 