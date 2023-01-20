#        TASK №3
to_ask = input("Enter sentence:")
replacement = input("Enter new delimeter:")  # replecement - замена
empty = " "
return_answer = to_ask.replace(empty, replacement)
result = return_answer
print("Result", result)

#        TASK №4
Digits1 = [1, 3, 5]
Digits2 = [2, 4, 6]
answer = Digits1[0] + Digits2[0]
print(answer)
answer = Digits1[1] + Digits2[1]
print(answer)
answer = Digits1[2] + Digits2[2]
print(answer)


#        TASK №5

list_1 = [12, 13, 1, 65, 45, 87, 121, 532, 1231, 10]
reverse = list_1[::-1]
print(reverse)