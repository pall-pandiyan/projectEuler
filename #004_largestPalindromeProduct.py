# Largest palindrome product

# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from math import sqrt, ceil

def isPolindrome(value):
    sTarget = str(value)
    n = len(sTarget)
    return sTarget == sTarget[n-1::-1]


def isProductOf3(value):
    r = 2
    while r*r<=value:
        if value%r == 0 and len(str(r))==3 and len(str(value//r))==3:
            return True
        r = r+1
    return False


if __name__ == "__main__":
    mul1 = 999
    mul2 = 999
    target = mul1 * mul2
    
    for i in range(target, 1, -1):
        if isPolindrome(i) and isProductOf3(i):
            print(f"The largest polindrome: {i}")
            break
            

# Sample:

# The largest polindrome: 906609