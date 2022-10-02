# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonachi(num):
    fibonachi_list = [0, 1]
    for i in range(num - 1):
        fibonachi_list.append(fibonachi_list[i] + fibonachi_list[i + 1])
    return fibonachi_list


def negofibonachi(num):
    fibonachi_list = [0, 1]
    for i in range(num - 1):
        fibonachi_list.append(fibonachi_list[i] - fibonachi_list[i + 1])
    fibonachi_list.reverse()
    return fibonachi_list[:-1]


def full_fibonachi(num):
    half_list1 = fibonachi(num)
    half_list2 = negofibonachi(num)
    full_list = half_list2 + half_list1
    return full_list


x = full_fibonachi(8)
print(x)
