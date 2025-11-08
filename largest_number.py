a, b, c = map(int, input("Enter three numbers: ").split())


if a > b and a > c:
    print(f"Largest: {a}")
elif b > a and b > c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")
