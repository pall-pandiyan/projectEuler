def isPrime(i):
    r = 2

    while r*r <=i:
        if i%r == 0:
            return False
        r = r+1
    
    return True


def nthPrime(n):
    i = 1
    
    while n:
        i = i+1
        if isPrime(i):
            n = n-1
    return i


if __name__ == "__main__":
    # n = int(input("Enter the value: ").strip())
    n = 10001
    print(f"{n}th prime number is {nthPrime(n)}")


# Sample:

# 10001th prime number is 104743