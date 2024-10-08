import math

def diskriminant(a, b, c):
    # Дискриминант
    D = b**2 - 4 * a * c
    if D > 0:
        # Два корня
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif D == 0:
        # Один корень
        x = -b / (2 * a)
        return (x)
    else:
        # Нет действительных корней
        return None
    
def main():
    # Ввод коэффициентов
    a = float(input("Введите коэффициент a (a != 0): "))
    while a == 0:
        print("Коэффициент a не должен быть равен 0. Пожалуйста, введите снова.")
        a = float(input("Введите коэффициент a: "))
    
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    korni = diskriminant(a, b, c)

    # Вывод результатов
    if korni is None:
      print("Уравнение не имеет действительных корней.")
    elif len(korni) == 1:
     print(f"Уравнение имеет один корень: x = {korni[0]}")
    else:
      print(f"Уравнение имеет два корня: x1 = {korni[0]}, x2 = {korni[1]}")
      
if __name__ == "__main__":
    main()