def test(n):
    return ((n >= 100) and (n < 1000))

def num_digits(n):
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    return a +  b + c 

def product_digits(n):
    """Product of digits of an integer."""
    a = n // 100
    b = (n // 10) % 10 
    c = n % 10
    return a *  b * c

def abs(n):
    if n >= 0:
        return n
    else:
        return -n

def loop(n):
    n = abs(n)
    if num_digits(n) == product_digits(n):
        return n
    else:
        return loop(n+1)

print("Give a 3-digit number!")
n = int(input())  # Transform string entry to integer
if not test(n):
    raise Exception("Your number needs to be a 3-digit number!")
else:
    print(loop(n), "is the mystery number")
