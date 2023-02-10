# Program: Sorting Numbers

def sort_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[j] = numbers[i]
                numbers[i] = temp
        return numbers


numbers = [7, 5, 2, 4, 3, 9, 1, 8, 6]
sorted_numbers = sort_numbers(numbers)
print("Sorted Numbers:", sorted_numbers)
