import math
def square_root(a):
    b = input('please input a value for aquare\n')
    x = eval(b)
    if int(x) != x:
        print("not a integer!")
        return
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < 0.000001:
            break
        x = y
    return x

def test_square_root():
    str1 = "a" + " " * 8 + "mysqurt(a)" + " " * 8 + "math.squrt(a)" + " " * 8 + "diff"
    print(str1)
    str2 = "-" + " " * 8 + "-" * 10 + " " * 8 + "-" * 13 + " " * 8 + "-" * 4
    print(str2)
    for a in range(9):
        print('%.1f      %f          %f             %f' % ( (a + 1), square_root(a + 1), math.sqrt(a + 1), abs(square_root(a + 1) - math.sqrt(a + 1))))

def eval_loop():
    while(1):
        str = input('please input a expression\n')
        if ( str == 'done' ):
            break
        x = eval(str)
        print(x)

def factorial(n):
    if 0 == n:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

    return total
