#генератор списков List comprehensions
a = [x for x in range(10)]
#print(a)

b = [x for x in range(10) if x % 3 == 0]
#print(b)

c = [x for x in range(10) if x % 3 == 0 or x % 2 == 0]
print(c)

d = 'Python is the best language'
d = d.split()
#print(d)

e = [x for x in d if len(x) > 3]
#print(e)

f = [x if len(x) > 3 else 'short' for x in d]
#print(f)

g = [x for x in range(10) if x % 2 == 0]
#print(g)

#как быстро выполняется генератор списков определение времени выполнения
import time
start_time = time.time()
russian_cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород', 'Челябинск', 'Самара', 'Омск', 'Ростов-на-Дону']
h = [x for x in russian_cities if len(x) >= 6]
print(h)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")


