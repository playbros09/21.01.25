#1. Створити список з 5 чисел, а потім вивести його у зворотному порядку.

a = [1,2,3,4,5]
for i in range (len(a)):
    print(a[-i-1],end=" ")
