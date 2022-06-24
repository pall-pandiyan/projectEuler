"""
Special Pythagorean triplet

Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_triplet(target):
    for a in range(1,target):
        for b in range(a+1,target):
            c = target - a - b
            if (a*a)+(b*b) == c*c:
                print(f"A: {a}  B: {b}  C: {c}")
                print("(a*a)+(b*b) = (c*c)")
                print(f"{a*a} + {b*b} = {(a*a)+(b*b)} = {c*c}")
                print(f"Product of abc: {a*b*c}")
                return


if __name__ == "__main__":
    # target = int(input("Enter the target: ").strip())
    target = 1000
    find_triplet(target)


# Sample:

# A: 200  B: 375  C: 425
# (a*a)+(b*b) = (c*c)
# 40000 + 140625 = 180625 = 180625
# Product of abc: 31875000