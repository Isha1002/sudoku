
import random

buttons=[[0 for i in range (9)]for j in range(9)]
buttons[0][0]=random.randint(1,9)


def is_valid(buttons,r,c,k):
    not_in_row=k not in buttons[r]
    not_in_col=k not in [buttons[i][c] for i in range (9)]
    not_in_box=k not in [buttons[i][j] for i in range (r//3*3,r//3*3+3) for j in range (c//3*3,c//3*3+3)]
    return not_in_row and not_in_col and not_in_box

def solve(buttons,r=0,c=0):
    if r==9:
        return True
    elif c==9:
        return solve(buttons,r+1,0)
    elif buttons[r][c]!=0:
        return solve(buttons,r,c+1)
    else:
        for k in range(1,10):
            if is_valid(buttons,r,c,k):
                buttons[r][c]=k
                if solve(buttons,r,c+1):
                    return True
                buttons[r][c]=0
        return False

solve(buttons)
for i in range(9):
    for j in range(9):
        print(buttons[i][j],end=" ")
    print("\n")

