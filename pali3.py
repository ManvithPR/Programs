n = 5

for i in range(1, n + 1):
    if i % 2 == 0:
        print(*range(i, 0, -1))
    else:
        print(*range(1, i + 1))