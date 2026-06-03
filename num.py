n = int(input("Enter Number: "))

# Perfect Number: sum of proper divisors equals the number
perfect = sum(i for i in range(1, n) if n % i == 0) == n

# Niven Number: divisible by sum of its digits
digit_sum = sum(int(d) for d in str(n))
niven = n % digit_sum == 0

# Buzz Number: divisible by 7 or ends with 7
buzz = n % 7 == 0 or n % 10 == 7

# Automorphic Number: square ends with the number itself
automorphic = str(n ** 2).endswith(str(n))

# Duck Number: contains at least one zero (not leading)
duck = '0' in str(n)[1:]

# Square-Free Number: not divisible by any perfect square > 1
square_free = all(n % (i * i) != 0 for i in range(2, int(n ** 0.5) + 1))

# Display results
checks = [
    (automorphic,  "Automorphic Number"),
    (perfect,      "Perfect Number"),
    (niven,        "Niven Number"),
    (buzz,         "Buzz Number"),
    (duck,         "Duck Number"),
    (square_free,  "Square-Free Number"),
]

for result, label in checks:
    print(label if result else f"Not {label}")