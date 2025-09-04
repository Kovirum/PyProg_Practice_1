print("Введите a, b, c")
a, b, c = map(int, input().split(' '))

print(f"{a=} {b=} {c=}")

d = b**2 - 4*a*c
print(d)