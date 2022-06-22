def gcd(a, b):
    while b:
        temp = b
        b = a%b
        a = temp
    return a


def lcm(a, b):
    return a*b // gcd(a,b)


def smallestMultiply(value):
    result = lcm(1,2)
    for i in range(3,value+1):
        result = lcm(result,i)
    print(f"The smallest product of {value} is {result}")


if __name__ == "__main__":
    # value = int(input("Enter the value: ").strip())
    value = 20
    smallestMultiply(value)


# Sample:

# The smallest product of 20 is 232792560