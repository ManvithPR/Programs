n = int(input("Enter a number: "))

for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    row = list(range(1, i)) + [i] + list(range(i - 1, 0, -1))
    print(*row)