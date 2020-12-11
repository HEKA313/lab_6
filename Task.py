import sys

name_file = sys.argv[1]  # Чтение командной строки

file = open(name_file, 'r')  # Открытие файла для чтения

n = int(file.readline())  # Ввод стороны квадратной матрицы
print("Сторона матрица равна: {}".format(n))

a = [[0] * n for i in range(n)]  # инициализация массива

for i in range(n):  # Ввод массива
	_ = file.readline().split()
	for j in range(n):
		a[i][j] = int(_[j])

for i in range(n):  # Вывод массива
	for j in range(n):
		print("%3d" % a[i][j], end='')
	print()

ans = [0] * n  # Конечный массив
prod = 1  # Произведение элементов матрицы

for i in range(n):  # перебор строк и счетчик строк
	aver = 0
	for j in range(n):  # перебор элементов строки
		if a[i][j] > 0:  # условие для среднего арифметического
			ans[i] += a[i][j]  # накопление среднего арифметического
			aver += 1  # счетчик для элементов среднего арифметического
		prod *= a[i][j]  # произведение элементов
	if aver != 0:
		ans[i] /= aver

print("Произведение элементов матрицы: {}".format(prod))
print("Массив со средним арифметическим положительных элементов: {}\n".format(ans))
