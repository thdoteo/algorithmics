"""Prints list to nine.

Asks user for a 2-digit number and prints successive
outputs of list to nine algorithm.

"""
def abs(n):
    """Computes absolute value of number."""
    if n > 0:
        return n
    else:
        return -n

def mirror(n):
    """Computes mirror number of a 2-digit number."""
    return (n % 10)*10 + (n // 10)

def list_to_nine(n):
    """Prints out list to nine intermediate results."""
    if n < 10:
        print(n)
    else: 
        print(n, end=", ")
        n = abs(n - mirror(n))
        list_to_nine(n)

n = int(input("Give me a positive 2-digit integer : "))
if n < 10 or n > 99:
    raise Exception("Not a 2-digit positive integer.")
else:
    list_to_nine(n)
    
    
    
    
