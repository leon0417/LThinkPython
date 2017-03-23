

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def compare(x, y, z):
    return x <= y <= z

def ack(m, n):
    if 0 == m:
        return n + 1
    elif m > 0 and 0 == n:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if 0 == len(word) or 1 == len(word):
        return True
    else:
        if first(word) == last(word) and is_palindrome(middle(word)):
            return True
        else:
            return False

def is_pow(a, b):
    if 1 == a:
        return True
    elif 0 == a % b and is_pow( a / b, b ):
        return True
    else:
        return False

def GCD(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return GCD(b, r)