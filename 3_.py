#3. Написати програму, яка пропонує користувачу ввести число і потім підраховує, скільки разів це число зустрічається у списку зі 100 випадкових елементів.
import random
import array


num = int(input("Введіть число: "))
add=0
b = []

sum = 0

for i in range(100):
    a = random.randint(1,99)
    b.extend([a])


for number in range(len(b)):

    if num == b[number]:
        sum = sum+1

print("Знайшло: ",sum)