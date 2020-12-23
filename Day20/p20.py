def parseInput(lines):
    tiles = {}
    readingTile = False
    lastTile = None
    for l in lines:
        if l == '':
            readingTile = False

        if readingTile:
            tiles[lastTile].append(l.strip())

        if "Tile" in l:
            lastTile = int(l.replace('Tile ','').replace(':','').strip())
            tiles[lastTile] = []
            readingTile = True

    return tiles

#Returns a dictionary with a the number of the tile as the key and
# the 4 borders of it as a list of strings(borders)
def getBorders(tiles):
    borders = {}
    for tile in tiles:
        borders[tile] = []
        
        n = tiles[tile][0]
        s = tiles[tile][-1]

        e,w = [],[]
        for row in tiles[tile]:
            e.append(row[0])
            w.append(row[-1])
        
        e = ''.join(e)
        w = ''.join(w)

        borders[tile].append(n)
        borders[tile].append(s)
        borders[tile].append(e)
        borders[tile].append(w)
    return borders

#Returns True if the border is equal to one the borders 
# (or reversed borders) of another tile 
def compareBorder(border1, borders2):   
    for b2 in borders2:
        if border1 == b2 or border1 == b2[::-1]:
            return True
    return False

#Problem 20 solution (part 1) 
def p20(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]  
        borders = getBorders(parseInput(lines))

        result = 1
        for t1,b1 in borders.items():
            repeated = [False, False, False, False]
            
            for t2,b2 in borders.items():
                if t1 != t2:
                    if repeated[0] != True and True == compareBorder(b1[0],b2):
                        repeated[0] = True

                    if repeated[1] != True and True ==  compareBorder(b1[1],b2):
                        repeated[1] = True

                    if repeated[2] != True and True ==  compareBorder(b1[2],b2):
                        repeated[2] = True

                    if repeated[3] != True and True ==  compareBorder(b1[3],b2):
                        repeated[3] = True

            if repeated.count(False) == 2:
                result *= t1

        return result
                           
 

#Problem 20 solution (part 2) 
#TODO: this part D:


#Main
result = p20('input.txt')   
print("P20 ->", result)
