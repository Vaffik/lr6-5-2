'''Написать программу, которая:
- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
- Выводит данную матрицу в форматированном виде
- Выводит сумму всех элементов отрицательных
'''
import random 

numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #необходимые для заполнения числа
k = 0 #сумма отрицательных
s = list() #строка матрицы
n = int(random.random() * 5 + 4) #количество столбцов матрицы
m = int(random.random() * 5 + 4) #количество строк матрицы
for i in range(n):
    s = [random.choice(numbers) for i in range(m)] #строка заполняется рандомными числами из списка
    print(*s) #строка выводится
    for j in s:
        k += (j if j < 0 else 0) #прибавляются числа меньше нуля из строки
print (f"Сумма отрицательных чисел {k}")#сумма выводится на экран