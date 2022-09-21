#Python Assessments_12, problem 2

''' Question: The chess king moves horizontally, vertically and diagonally, but only 1 square. Given two
different cells on a chessboard, determine if the king can get from the first cell to the second
in one move. The program receives as input four numbers from 1 to 8 each, specifying the
column number and row number, first for the first cell, then for the second cell. The program
should output YES if it is possible to get to the second cell from the first cell by the king's
move, or NO otherwise. '''


def xcell(x1,x2):
    x=0
    if x1 -x2 > 0:
        x = x1 - x2
    elif  x1-x2 < 0:
        x = x2-x1
    else: x
    return x
    
def ycell(y1,y2):
    y=0
    if y1 -y2 >= 0:
        y = y1 - y2
    elif  y1-y2 < 0:
        y = y2-y1
    else: y
    return y
    
x1 = 4
y1 = 5
x2 = 5
y2 = 4    
    
if ((xcell(x1,x2) == 1) & (ycell(y1,y2) == 0))or ((xcell(x1,x2) == 0) 
        (ycell(y1,y2) == 1))or((xcell(x1,x2) == 1) & (ycell(y1,y2) == 1)):
         print("YES")
else: print("NO")
