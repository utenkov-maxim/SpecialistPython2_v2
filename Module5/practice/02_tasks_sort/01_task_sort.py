# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10  # Задайте самостоятельно, выбрав произвольное число

# var 1
summa = 0
for n in numbers:
    if n > a:
        summa += n

print(summa)

# var 2

print(sum([n for n in numbers if n > a]))