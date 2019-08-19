'''
You are given a 2D array of characters, and a target string.
Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.
'''

def validate_word(matrix, word, i, j):
    found_row = True
    found_column = True

    for k in range(len(word)):
        found_row = found_row and (matrix[i][j+k] == word[k])
        found_column = found_column and (matrix[i+k][j] == word[k])

    return found_row or found_column

def word_search(matrix, word):
    first_letter = word[0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == first_letter):
                found = validate_word(matrix, word, i, j)
                if (found):
                    return True
    return False

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print (word_search(matrix, 'FOAM'))
# True
