from random import randint

while True:
    try:
        a=int(input("Введите количесвто строк "))
        b=int(input("Введите количесвто столбцов "))
        break
    except ValueError:
        print("введеныне корректные данные")
arr = []
coord = {}
for i in range(a):
    string = []
    for j in range(b):
        rand_int = randint(-10000, 10000)
        string.append(rand_int)
        coord[(j+1, i+1)] = rand_int
    arr.append(string)
arr_trans = []

# for i in range(len(arr[0])):
#     new_string = []
#     for j in range(len(arr)):
#         new_string.append(arr[j][i])
#     arr_trans.append(new_string)

for i in arr:
    print(i)
print()

min_el_in_str = []
max_el_in_row = []
for i in range(len(arr)):
    min_el_in_str.append(min(arr[i]))

for i in range(len(arr[0])):
    els_in_row = []
    for j in range(len(arr)):
        els_in_row.append(arr[j][i])
    max_el_in_row.append(max(els_in_row))

# print(min_el_in_str)
# print(max_el_in_row)
for i in max_el_in_row:
    if i in min_el_in_str:
        # print(i)
        for key, val in coord.items():
            if val == i:
                print(key, i)
        break
        # print(max_el_in_row)
# print(coord)
# for key, val in coord.items():
#     print(key, val)
# for i in arr_trans:
#     print(i)
#
# for i in range(len(arr)):
#     print(min(arr[i]), max(arr_trans[i]))

# for i in range(len(arr)):
#     print(arr[i])

# for i in arr:
#     print(i)
#
# # print(arr[0][1])
# ans = []
# c = 0
# for i in range(len(arr)):
#     ans.append((arr[i][i], (i+1, i+1)))
#     c += 1
#
# print()
# for i in ans:
#     print(i)
