'''board = [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]


flag=True
def validsudoku():
    for row in board:
        for i in range(9):
            if row[i]!='.':
                if not any(row.count(row[i]) > 1 for element in row):
                    iterate=0
                    for j in range(9):
                        if board[j][i]==row[i]:
                            iterate+=1
                            if iterate>1:
                                return False
                else:
                    return False
    return True
                        

print(validsudoku())'''

a=10
b=30.3
c="Python"
print(type(a))
print(type(b))
print(type(c))






