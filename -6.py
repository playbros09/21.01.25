#6. Реалізувати програму-лотерею. Програма загадує 5 випадкових унікальних чисел у діапазоні від 1 до 42, але не показує їх на екран. Користувач намагається їх вгадати – вводить свої 5 чисел із клавіатури. Призначити призи за збіги: наприклад, якщо користувач вгадав три числа – приз 100 гривень, якщо 4 – 500 гривень, якщо 5 – 2500 гривень.
import random

m = [0,0,0,0,0]
rand = [0,0,0,0,0]
all=0

for num in range(5):
    m[num] = int(input("Введіть число: "))

for i in range(5):
    l = random.randint(1, 42)
    rand[i] = l

print(rand)
for a in range(4):
    for b in range(4):
        if m[a]==rand[b]:
            all=all+1
print(all)
if all == 0:
    print("0 гривень")
elif all == 1:
    print ("25 гривень")
elif all == 2:
    print ("50 гривень")
elif all == 3:
    print ("100 гривень")
elif all == 4:
    print ("500 гривень")
elif all == 1:
    print ("2500 гривень")