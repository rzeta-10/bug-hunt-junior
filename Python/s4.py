# Program: Check if an integer is a power of 2

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n-1)) == 1


num = 69
if is_power_of_two(num):
    print(num, "is a power of 2")
else:
    print(num, "is not a power of 2")
