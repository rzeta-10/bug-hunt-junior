# Program: Permutes a list of numbers
# Description:
#   - A list of distinct numbers is stored in data
#   - All possible permutations of the list is found using the recursive function permute

def permute(data, i, length, result):
    if i == length:
        result.append(data)
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length, result)
            data[i], data[j] = data[j], data[i]


def main():
    data = [1, 2, 3]
    length = len(data)
    result = []
    permute(data, 0, length, result)
    print(result)


if __name__ == "__main__":
    main()
