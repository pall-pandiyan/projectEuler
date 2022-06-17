if __name__ == "__main__":
    target = 4000000
    a = 1
    b = 2
    fib = 2
    sum = 0

    while(fib<target):
        if fib%2 == 0:
            sum = sum + fib
        fib = a+b
        a = b
        b = fib
    print(sum)


# Sample:

# 4613732