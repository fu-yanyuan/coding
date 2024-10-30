# gcd(0, x) = x

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


        