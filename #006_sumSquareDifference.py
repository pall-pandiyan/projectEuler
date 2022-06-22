def sumSquareDifference(value):
    square_sum = 0
    sum = 0
    for i in range(1,value+1):
        sum = sum+i
        square_sum = square_sum + (i*i)
    
    sum_square = sum*sum
    return sum_square - square_sum


if __name__ == "__main__":
    # value = int(input("Enter the value: ").strip())
    value = 100
    print(f"difference between sum square and square sum of {value} is {sumSquareDifference(value)}")


# Sample:

# difference between sum square and square sum of 100 is 25164150