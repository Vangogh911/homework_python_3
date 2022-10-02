# НЕОБЯЗАТЕЛЬНОЕ ЗАДАНИЕ
# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time


def random_generator(max_edge, min_edge=0):
    # Количество итераций для получения более неровномерных значений
    iteration = 7
    # Вычисление наименьшей составной еденицы псевдослучайного числа
    unit = ((max_edge - min_edge) / 100)
    # Вычисление среднего значения псевдослучайного элемента с помощью системного времени
    buf = 0
    for j in range(iteration):
        random_element = round(time.perf_counter_ns() / 100 % 100)
        buf += round(random_element, 1)
    buf /= iteration
    # Вычисление псевдослучайного числа в заданных пределах
    return round((buf * unit) + min_edge, 1)


arr = []
for i in range(10):
    arr.append(random_generator(100))
print(arr)

arr2 = []
for i in range(10):
    arr2.append(random_generator(1000, 500))
print(arr2)

# Не очень доволен результатом, но нет времени на доработку в данный момент
