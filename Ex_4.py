# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_to_bin(num):
    binary_list = []
    while num >= 2:
        binary_list.append(int(num % 2))
        num = int(num / 2)
    else:
        binary_list.append(num)
    binary_list.reverse()
    for i in binary_list:
        print(i,  end="")
    print()


convert_to_bin(45)
convert_to_bin(3)
convert_to_bin(2)
