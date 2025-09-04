def math_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    print(d)

    if d > 0:
        print("Дискриминант больше 0 - 2 действительных корня")
        print(f"x1 = {-b-d**0.5/(2*a)}, x2 = {-b+d**0.5/(2*a)}")
    elif d == 0:
        print("Дискриминант равен 0 - 1 действительный корень")
        print(f"x = {-b/2*a}")
    else:
        print("Дискриминант меньше 0 - действительных корней нет")
        return


print("Введите a, b, c")
a, b, c = map(int, input().split(' '))

print(f"{a=} {b=} {c=}")

math_roots(a, b, c)

