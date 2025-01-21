#4. Створити список із 200 випадкових чисел у діапазоні від 0 до 200. Визначити кількість однозначних, двозначних і тризначних чисел у відсотковому співвідношенні.
import random
import array


add=0
b = []

one=0
two=0
three=0

for i in range(200):
    a = random.randint(1,200)
    b.extend([a])


for number in range(len(b)):
    add = b[number]
    if add%100==0:
        one = one+1
    elif add%10==0:
        two = two+1
    elif add%1==0:
        three = three+1
    
print("1: ",one/2,"% 2: ",two/2,"% 3: ",three/2,"%")