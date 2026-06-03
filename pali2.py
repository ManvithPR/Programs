n = int(input("Enter a number: "))

for i in range(1, n + 1):
    row = list(range(i, i + i - 1)) + [i + i - 1] + list(range(i + i - 2, i - 1, -1))
    print(*row)