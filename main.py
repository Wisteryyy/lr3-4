import math
a=float(input("Введите первый коэффициент: "))
b=float(input("Введите второй коэффициент: "))
c=float(input("Введите третий коэффициент: "))

def diskriminant(a,b,c):
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return (x)
    else:
        return None

korni = diskriminant(a, b, c)

if korni is None:
    print("Уравнение не имеет корней")
elif len(korni) == 1:
    print(f"Уравнение имеет один корень: x = {korni[0]}")
else:
    print(f"Уравнение имеет два корня: x1 = {korni[0]}, x2 = {korni[1]}")
