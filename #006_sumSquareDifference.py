"""
The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385$$

The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

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