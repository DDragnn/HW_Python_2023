# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


n = int(input("Введите количество журавликов: "))
if n // 6 and n % 2 == 0:
    petr = n // 6
    serg = n // 6
    kate = (petr + serg) * 2
    print(petr, kate, serg)
else:
    print('Попробуйте еще раз')

