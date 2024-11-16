fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "pear", "peach", "plum"]

#for index, fruit in enumerate(fruits):
#    print(f"Index: {index}, Fruit: {fruit}")

#for index, fruit in enumerate(fruits, start=1):
#    print(f"Index: {index}, Fruit: {fruit}")

for i in enumerate(fruits):
    print(i[0], i[1])
