# Program: Count letters and digits in a sentence

sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
    if char.isdigit():
    	digit_count += 1
    elif char.isalpha():
    	letter_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)
