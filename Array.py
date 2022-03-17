import random

n = int(input('Tedad anasor arraye ra vared konid...: '))

array = []
i = 0
while i < n:
    number = random.randint(0,1000)
    if number not in array:
        array.append(number)
        i += 1
print(array)
