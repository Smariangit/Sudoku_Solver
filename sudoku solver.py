board=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]
       ]

def bo():
    l=[]
    for i in range(9):
        x=[int(a) for a in input()]
        l.append(x)
    global board
    board=l

def prbo():
    for i in range(9):
        if i%3==0 and i!=0:
            print('--------------------------------')
        #else
        for j in range(9):
            if j%3==0 and j!=0:
                print(' | ',end='')
            if j==8:
                print(board[i][j])
            else:
                print(board[i][j],' ', end='')


def possible(x,y,n):
    global board
    for i in range(9):
        if board[x][i]==n:
            return False

    for i in range(9):
        if board[i][y]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if board[x0+i][y0+j]==n:
                return False
    return True
    

def solve():
    global board
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for n in range(1,10):
                    if possible(i,j,n):
                        board[i][j]=n
                        solve()
                        board[i][j]=0
                return
    print('\n\nThe final board is-')
    prbo()

def main():
    print('Input the board')
    bo()
    print('The initial board is- ')
    prbo()
    solve()

if __name__=='__main__':
    main()


