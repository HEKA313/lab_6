import sys

name_file = sys.argv[1]  # Чтение командной строки

file = open(name_file, 'r')  # Открытие файла для чтения

n = int(file.readline())  # Ввод стороны квадратной матрицы
print("Сторона матрица равна: {}".format(n))

a = [[] for i in range(n)]  # инициализация массива
for i in range(n):  # Ввод массива
	for elem in file.readline().split():
		a[i].append(int(elem))

for row in a:  # Вывод массива
	for col in row:
		print("%3d" % col, end='')
	print()

x = int(file.readline())  # Ввод номера строки для среднего арифметического
print("Номер строки для среднего арифметического равна: {}".format(x))

ans = []  # Конечный массив
aver = i = 0  # Среднее арифметическое и их счетчик
prod = 1  # Произведение элементов матрицы

for i, row in enumerate(a):  # Подсчет произведения и среднего арифметического
	for col in row:
		if i == (x - 1) and row > 0:
			aver += row
			i += 1
		ans.append(col)
		prod *= col

check_positive = True

if i != 0:  # Проверка на количество чисел в среднем арифметическом
	aver /= i  # Нахождение среднего арифметического
else:
	check_positive = False

print("Массив: {}\nПроизведение элементов матрицы: {}".format(ans, prod))
if check_positive:
	print("Среднее арифметическое положительных элементов {} строки: {}\n".format(x, aver))
else:
	print("Положительных элементов в {} строке не найдено\n".format(x))
