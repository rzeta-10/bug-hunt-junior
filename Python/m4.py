# Program: Convert any decimal number to binary number (approx.)

def decimal_to_binary(decimal_num):
    binary = ""
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part = integer_part // 2
    #binary = "." + binary
    while fractional_part > 0:
        fractional_part *= 2
        binary += str(int(fractional_part))
        fractional_part = fractional_part - int(fractional_part)
    return binary


decimal = float(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print("Binary equivalent of", decimal, "is", binary)
