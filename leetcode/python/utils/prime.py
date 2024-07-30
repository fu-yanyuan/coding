import math

def isPrime(n):
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i + 1) == 0:
            return False
    
    return True

def isPrime2(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True


def countPrimes(n):
    """
    return number of primes in the range [0, n)
    """
    if n <= 1:
        return 0
    
    isPrime = [1] * (n)
    isPrime[0] = 0
    isPrime[1] = 0

    ans = 0
    for i in range(2, n):
        if isPrime[i]:
            ans += 1
            for i in range(i * i, n, i):
                isPrime[i] = 0
    
    return ans

def countPrimes2(n):
    a=[0]*n
    ans=0
    for i in range(2,n):
        if a[i]:
            continue
        ans += 1
        a[i*i:n:i] = [1] * ((n-1) // i - i + 1)
    return ans