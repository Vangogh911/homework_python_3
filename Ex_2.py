# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mirror_mul(numbers):
    result_list = []
    for i in range(int(len(numbers) / 2)):
        j = (i + 1) * -1
        result_list.append(numbers[i] * numbers[j])
    if (len(numbers) % 2) != 0:
        i = (int(len(numbers) / 2))
        result_list.append(numbers[i]**2)
    return result_list


arr = [2, 3, 4, 5, 6]
mul_list = mirror_mul(arr)
print(mul_list)
arr2 = [2, 3, 5, 6]
mul_list2 = mirror_mul(arr2)
print(mul_list2)
