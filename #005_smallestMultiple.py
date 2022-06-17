def isPrime(num):
    r = 2
    while r*r<=num:
        if num%r == 0:
            return False
        r = r+1
    return True


def minMaxValue(target):
    result = [1,1]
    for i in range(2,target+1):
        result[1] = result[1]*i
        if isPrime(i):
            result[0] = result[0]*i
    return result


def needCorrection(target, current, table):
    flag = False
    for i in range(2, target+1):
        if current%i > 0:
            table[i-1] = 0
            flag = True
            break
        else:
            table[i-1] = 1
    return flag


def main(value):
    min1, max1 = minMaxValue(value)
    table = [0]*value
    # print(f"minimum: {min1}  maximux: {max1}")
    current = min1*2

    while needCorrection(value, current, table):
        if current < max1:
            print(f"{current} {table} {min1} {max1}")
            current = current+1
        else:
            current = max1
            break

    print("Smallest product:", current)


if __name__ == "__main__":
    main(10)


# Sample:
