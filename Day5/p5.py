import re
  
#Problem 5 solution (part 1)
def binaryRowSearch(row, remainingRows):
    if not row or len(remainingRows) == 1:
        return remainingRows[0]
    else:
        if row[0] == 'F':
            remainingRows = [remainingRows[0], int((remainingRows[0] + remainingRows[1])/2)]
            
        elif row[0] == 'B':
            remainingRows = [int((remainingRows[0] + remainingRows[1])/2)+1, remainingRows[1]]
            
        return binaryRowSearch(row[1:], remainingRows)    
    
def binaryColumnSearch(column, remainingColumns):
    if not column or len(remainingColumns) == 1:
        return remainingColumns[0]
    else:
        if column[0] == 'L':
            remainingColumns = [remainingColumns[0], int((remainingColumns[0] + remainingColumns[1])/2)]
            
        elif column[0] == 'R':
            remainingColumns = [int((remainingColumns[0] + remainingColumns[1])/2)+1, remainingColumns[1]]
            
        return binaryColumnSearch(column[1:], remainingColumns)  
    
#1rst part solution
def p5(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        ids = []
        for l in lines: 
            rowDir = l[:-3]
            columnDir = l[-3:]
            rowsRange = [0,127]
            columnsRange = [0,7]
            
            passRow = binaryRowSearch(rowDir,rowsRange)
            passColumn = binaryColumnSearch(columnDir, columnsRange)
            passID = 8*passRow + passColumn
            ids.append(passID)
        
        return max(ids), ids
        
        
#Problem 5 solution (part 2)
def p5_2(ids):
    for id in ids:
        myMissingID = id+1
        myOtherCloseID = id+2
        if myMissingID not in ids and myOtherCloseID in ids:
            return myMissingID
           
        
#Main
result, ids = p5('input.txt')
print("P5 ->",result)

result = p5_2(ids)
print("p5_2 ->", result)