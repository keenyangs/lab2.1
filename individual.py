# Программа для вычисления времени встречи двух автомобилей

# Запрос входных данных
v1 = int(input("Введите скорость первой машины (км/ч): "))
v2 = int(input("Введите скорость второй машины (км/ч): "))
S = int(input("Введите расстояние между автомобилями (км): "))

# Вычисление времени встречи
t = S / (v1 + v2)

# Вывод результата на экран
print("Время встречи автомобилей составит", t, "часов.")