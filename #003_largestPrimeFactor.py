# Largest prime factor

# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def isPrime(target):
    r = 2
    while (r*r <= target):
        if target%r == 0:
            return False
        r = r+1
    return True

def largestPrime(target):
    prime_factors = []
    i=2
    while(i*i <= target):
        if target%i == 0:
            if isPrime(i):
                prime_factors.append(i)
            if isPrime(target//i):
                prime_factors.append(target//i)
        i = i+1
    print("prime factores:", prime_factors)
    print("biggest prime factors:", max(prime_factors))


if __name__ == "__main__":
    target = 600851475143
    largestPrime(target)


# Sample:

# prime factores: [71, 839, 1471, 6857]
# biggest prime factors: 6857