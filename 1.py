lst = [2, -1, 5, -5, 4]
summa = 0
for i in range(1, len(lst), 2):
    if i % 2 != 0:
        summa = summa + lst[i]
print(summa)
