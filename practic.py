# task 1

lis_t = [
    11, 22, 33.4, 52, 26, 27,
    28, 19, 101, 110, 12, 1, 12.3,
]
count = int(len(lis_t))
print(count)


# 1 method find last element
last = lis_t[-1]
print(last)
# 2 method find last element
last_2 = lis_t[len(lis_t) - 1]
print(last_2)

# Find first elm
elm = lis_t[len(lis_t) - 2]
print(elm)


# Find averege element
index_middle = count//2
print(lis_t[index_middle])

#
reversed_list1 = reversed(lis_t)
print(reversed_list1)
reversed_list2 = lis_t[::-1]
print(reversed_list2)

#
sorted_list1=list(sorted(lis_t))
print(sorted_list1)
# sort and edit list
lis_t.sort()
print(lis_t)
#
max_number = lis_t[-1]
print(max_number)

minimum_num = lis_t[0]
print(minimum_num)

middle_value = sum(lis_t)/len(lis_t)
print(middle_value)

max_before_elm= lis_t[-2]
print(max_before_elm)

#    task 2

ls = [8, 9, 10]
# Добавляем 17
ls[1] = 17
# Добавляем в конец 4,5,6,
ls.append(4)
ls.append(5)
ls.append(6)

# Удаляем первый элемент
ls.pop(0)

# сортируем список
ls.sort()

# Добавляем такой же список
ls.extend(ls)
print(ls)





