def isPrime(num):
    if num<2:
        return False
    r = 2
    while r*r <= num:
        if num%r == 0:
            return False
        r = r+1
    return True

    # for i in range(2,(num//2)+1):
    #     if num%i == 0:
    #         return False
    # return True


def sum_of_primes(target):
    result = 0
    for i in range(1, target):
        if isPrime(i):
            result = result+i
    return result


if __name__ == "__main__":
    target = 2000000
    print(f"The target is {target}")
    print(f"Sum of Primes: {sum_of_primes(target)}")


# Sample:

# The target is 2000000
# Sum of Primes: 142913828922