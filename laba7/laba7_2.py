while True:
    try:
        M = int(input("Введите количесво строк: "))
        N = int(input("Введите количесво столбцов: "))
        break
    except ValueError:
        print("введеныне корректные данные")
matrix = [[i + j for j in range(1,N+1)] for i in range(1,M+1)]
sums = [sum(row) for row in matrix]
print("Исходная матрица:")
for row in matrix:
    print(row)
print("Суммы элементов каждой строки:", sums)