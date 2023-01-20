# [] -> список
# list()


# numbeee = list()
# numbeee.append(2) # добовляет элемент
# print(numbeee)
number = [1, 12, 132, 134, 123]
#    0   1    2    3    4

substring = number[1:3]
print(substring)

element = number.pop()  # delet element
print(element)

number.pop(2)
print(number)

fruets = ['apple', 'banana', 'cherry']
fruets.insert(1, 'orange')
print(fruets)

class_a = ['apple', 'banana', 'cherry']
class_b = ['aaa', 'aas', 'wqdw']
whole_class = list()


numbers = [1111111, 212, 22, 2]
print(sum(numbers))  # скаладывает числа
print(max(numbers))  # выводит максимальное число

num = [1, 2, 3, 4, 4]
num[4] = 5
num[len(num) - 1] = 0
print(num)
numb_tuple = (1, 2, 3)
numb_tuple = list(numb_tuple)
numb_tuple.append(4)
print(numb_tuple)




