# Program: Word Search in a 2D Matrix
# Description:
#   - A 2D matrix of characters and a target word is given
#   - The task is to find if the word exists in the matrix
#   - The word cane formed by moving up, down, left or right (not diagonally)

def search(matrix, word, i, j, k, visited):
    if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and visited[i][j]):
        return False
    if matrix[i][j] != word[k]:
        return False
    if k == len(word) - 1:
        return True
    visited[i][j] = True
    found = search(matrix, word, i - 1, j, k + 1, visited) or \
            search(matrix, word, i + 1, j, k + 1, visited) or \
            search(matrix, word, i, j - 1, k + 1, visited) or \
            search(matrix, word, i, j + 1, k + 1, visited)
    visited[i][j] = False
    return found


def word_search(matrix, word):
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if search(matrix, word, i, j, 0, visited):
                return True
    return False


matrix = [['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']
          ]
word = "SEE"

if word_search(matrix, word):
    print(f"'{word}' was found in the matrix.")
else:
    print(f"'{word}' was not found in the matrix.")
