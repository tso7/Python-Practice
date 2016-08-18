grid = [['.', '.', '.', '.', '.', '.','A'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def FlipGrid(grid):
    i = j = 0
    while i < len(grid) and j < len(grid[i]):
        print (grid[i][j], end='')
        if (i == len(grid)-1):
            j += 1
            i = 0
            print()
        else:
            i += 1

FlipGrid(grid)
        
