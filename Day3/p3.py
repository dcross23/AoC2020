import itertools

#Problem 3 solution (part 1)
def p3(fileName, slope):
    with open(fileName, 'r') as f:
        treeMap = [line.strip() for line in f]
        row, column = 0,0
        numTrees = 0
        numColumns = len(treeMap[row])

        while row < len(treeMap)-1:
            row = row + slope[0]
            column = column + slope[1]

            if treeMap[row][column % numColumns] == '#':
                numTrees += 1
        
    return numTrees

#Problem 3 solution (part 2)
def p3_2(fileName, slopes):
    result = 1
    for slope in slopes:
        sol = p3(fileName, slope)
        result *= sol
    
    return result

#Main
result = p3('input.txt', (1,3))
print("P3 ->",result)

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
result = p3_2('input.txt', slopes)
print("P3_2 ->", result)
    
