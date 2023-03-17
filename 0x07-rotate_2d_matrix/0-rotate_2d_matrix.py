#!/usr/bin/python3
'''Module to rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''
    Function to rotate a matrix
    Args:
      matrix (list[[list]]): a matrix
    '''
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
