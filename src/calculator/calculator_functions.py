# calculation_functions.py

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def factorize(n):
    """Return prime factors of n."""
    n = int(n)
    i, factors = 2, []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors