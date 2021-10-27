#name: Cassidy Ward
#date: 10/26/2021
#description: this program takes two positive integers as
# parameters and returns the product of those two numbers


def multiply(n1, n2):
    if n2 == 0:  
        return 0  
    else:  
        return n1 + multiply(n1, n2 - 1)  # n1 times n2 = n1 + (n1 times (n2-1))
