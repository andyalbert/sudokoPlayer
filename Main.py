import copy

initialSudoko = [[-1 for x in range(9)] for x in range(9)] # the table that carry initial sudoko

def getAvailableValues(currentSudoko, a, b): # function to get the available values for a single node of a sudoko
    availValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9): # checking column
        if currentSudoko[i][b] in availValues:
            availValues.remove(currentSudoko[i][b])
    
    for i in range(9): # checking row
        if currentSudoko[a][i] in availValues:
            availValues.remove(currentSudoko[a][i])
    
    row, coln =  (int) (a/3), (int) (b/3)
    row *= 3
    coln *= 3
    
    for i in range(row, row + 3): # for the current block
        for j in range(coln, coln + 3):
            if currentSudoko[i][j] in availValues:
                availValues.remove(currentSudoko[i][j])
    return availValues


def backtracking(board):
    ## first, check of completness
    for i in range(9):
        for j in range(9):
            if board[i][j] == -1:
                avail = getAvailableValues(board, i, j)
                if len(avail) == 0:
                    return [False, ""]
                for itirator in avail:
                    tempBoard = copy.deepcopy(board)
                    tempBoard[i][j] = itirator
                    val = backtracking(tempBoard)
                    if val[0] == True:
                        return val
    return [True, board]

# -----------------------Main--------------------------
i = -1
f = open("sudoko.txt", 'r+')
for line in f:
    i = i + 1
    values = line.split(',')
    for j in range(9):
        if values[j] != '_' and values[j] != '_\n':
            initialSudoko[i][j] = (int) (values[j])
        else:
            initialSudoko[i][j] = -1

#for i in range(9):
#    print(initialSudoko[i])
myResult = backtracking(initialSudoko)
if myResult[0] == True:
    for i in range(9):
        print(myResult[1][i])
else:
    print('not solvable !')