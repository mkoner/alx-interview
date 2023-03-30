#!/usr/bin/python3
'''
Island Perimeter
'''
def island_perimeter(grid):
    '''Function  that returns the perimeter of the island
    described in grid
    '''
    if type(grid) != list:
        return 0
    A = set()
    B = set()
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i not in A:
                    A.add(i)
                    perimeter += 2
                if j not in B:
                    B.add(j)
                    perimeter += 2
    return perimeter
