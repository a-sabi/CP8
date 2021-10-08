def to_bin(num10):
    ans = 0
    c = 1
    while num10 > 0:
        ans = (num10 % 2) * c + ans
        c = c * 10
        num10 = num10 // 2
    return ans

def to_oct(num10):
    ans = 0
    c = 1
    while num10 > 0:
        ans = (num10 % 8) * c + ans
        c = c * 10
        num10 = num10 // 8
    return ans

while True:
    try:
        d = int(input("Введите положительное десятичное число: "))
        if d < 0:
            raise Exeption()
        e = int(input("Введите в какую систему перевести (8 или 2): "))
        if e == 2:
            print(to_bin(d))
            break
        elif e == 8:
            print(to_oct(d))
            break
        else:
            raise Exeption()
    except:
        print("Ввод неправильный")
        continue
