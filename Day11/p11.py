def readMap(f):
    Map = []
    for line in f:
        Map.append([c for c in line.strip()])
    return Map

#generates positions in an especific direction until there is an occupied seat (# or L)
def getViewSeats(x,y, direction, Map):
    if direction == 'UL':
        while y-1 >=0 and x-1>=0:
            yield (x-1,y-1)
            y -= 1
            x -= 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'U':
        while x-1 >= 0:
            yield (x-1, y)
            x -= 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'UR':
        while y+1<len(Map[0]) and x-1>=0:
            yield (x-1,y+1)
            y += 1
            x -= 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'L':
        while y-1 >= 0:
            yield (x, y-1)
            y -= 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'R':
        while y+1 < len(Map[0]):
            yield (x, y+1)
            y += 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'DL':
        while y-1 >=0 and x+1<len(Map):
            yield (x+1,y-1)
            y -= 1
            x += 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'D':
        while x+1 < len(Map):
            yield (x+1, y)
            x += 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

    elif direction == 'DR':
        while y+1<len(Map[0]) and x+1<len(Map):
            yield (x+1,y+1)
            y += 1
            x += 1
            if (Map[x][y] == '#' or Map[x][y] == 'L'):
                break

#Gets the adyacents for both examples, inmediatly close to the seat(part 1) or next seat in the row/column/diagonal of the seat(part2)
def getAdyacents(x, y, Map, part):
    if part == 1:
        ady = [(x-1, y-1), (x-1, y), (x-1,y+1), (x, y-1), (x,y+1), (x+1, y-1), (x+1, y), (x+1,y+1)]
        ady = [ Map[pos[0]][pos[1]] for pos in ady if not (pos[0]<0 or pos[0]>=len(Map) or pos[1]<0 or pos[1]>=len(Map[0]))]
        return ady

    elif part == 2:
        allSeats = []
        for direction in ['UL','U','UR','L','R','DL','D','DR']:
            for l in list(getViewSeats(x, y ,direction, Map)):
                allSeats.append(Map[l[0]][l[1]])
        return allSeats


#Next iteration with the new map
def nextRound(Map, part):
    newMap = []
    for x,row in enumerate(Map):
        newLine = []
        for y, element in enumerate(row):
            if element == '.':
                newLine.append('.')

            elif element == 'L':
                if getAdyacents(x,y, Map, part).count('#') == 0:
                    newLine.append('#')
                else: 
                    newLine.append('L')
            
            elif element == '#':
                if part == 1:
                    num = 4
                elif part == 2:
                    num = 5

                ady = getAdyacents(x,y, Map, part)
                if ady.count('#') >= num:
                    newLine.append('L')
                else: 
                    newLine.append('#')

        newMap.append(newLine)
    return newMap


#Problem 11 solution (part 1)  
def p11(fileName, part):
    with open(fileName, 'r') as f:
        Map = readMap(f)        
        while(True):
            Map2 = nextRound(Map,part)  

            if(Map2 == Map):
                occupied = 0
                for l in Map2:
                   occupied += l.count('#')   
                return occupied

            else:
                Map = Map2

#Problem 11 solution (part 2)  
def p11_2(fileName, part):
    return p11(fileName, part)


#Main
result = p11('input.txt',1)
print("P11 ->", result)

result = p11_2('input.txt', 2)
print("P11_2 ->", result)