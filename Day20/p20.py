import math
import re
from tile import Tile

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

#This first try was okay but too slow. This was because for each tile that we want to 
# add to the drawing, we recalculate his possible arrangements each time and we compare each
# one with all the possibilities of the other tile. This is so slow, we are recalculating
# many times the possible tiles. 
#To solve this problem, I just had to calculate all possible tiles (rotated and fliped)
# one time and just compare strings instead of recalculating them for each iteration

#Slow solution
def getTiles(parsedLines):
    tiles = []
    for k,v in parsedLines.items():
        tiles.append(Tile(k,v))
    return tiles

def searchNextTile(row, col, grid, tiles):
    if(row == len(grid)):
        return True
    else:
        for tile in tiles:
            if not tile.isVisited():
                for i in range(2):
                    for _ in range(4):
                        if row>0 and not tile.matchesPossibilitiesBelow(grid[row-1][col].getFinalDrawing()):
                            tile.rotate()
                            continue
                        if col>0 and not tile.matchesPossibilitiesRight(grid[row][col-1].getFinalDrawing()):
                            tile.rotate()
                            continue

                        tile.setVisited(True)
                        grid[row][col] = tile

                        if col == len(grid[0])-1:
                            if(searchNextTile(row+1, 0, grid, tiles)):
                                return True
                        else:
                            if(searchNextTile(row, col+1, grid, tiles)):
                                return True

                        tile.setVisited(False)

                    tile.resetFinalDrawing()
                    if(i == 0):
                        tile.flip()
        return False

def p20_2_slow(fileName):
    with open(fileName, 'r')  as f:
        lines = [line.strip() for line in f] 
        tiles = getTiles(parseInput(lines))
        length = math.ceil(math.sqrt(len(tiles)))
        grid = [[Tile(0,[]) for x in range(length)] for y in range(length)]

        searchNextTile(0,0, grid, tiles)
        
        for row in grid:
            for t in row:
                print(t.getID())
                for l in t.getFinalDrawing():
                    print(l)
                print()




#-----------------------------------------------
#Correct solution
def rotate(tile):
    newTile = []
    for i in range(0,len(tile)):
        s = ''
        for t in reversed(tile):
            s += t[i]
        newTile.append(s);
    return newTile

def flip(tile):
    newTile = []
    for t in reversed(tile):
        newTile.append(t)
    return newTile


def getAllPossibleTiles(parsedLines):
    tiles = []
    numTiles = 0
    for k,v in parsedLines.items():
        numTiles += 1

        v2 = v.copy()
        for _ in range(2):
            for _ in range(4):
                tiles.append(Tile(k, v2))
                v2 = rotate(v2)
            v2 = flip(v2)

    return tiles, numTiles


def fastSearchNextTile(row, col, tiles, length, grid, visited):
    if(len(visited) == pow(length,2) or row == length):
        return True
    else:
        for tile in tiles:
            if(tile.getID() not in visited):
                if row>0 and not tile.matchesBelow(grid[row-1][col].getFinalDrawing()):
                    continue
                if col>0 and not tile.matchesRight(grid[row][col-1].getFinalDrawing()):
                    continue

                grid[row][col] = tile
                visited.append(tile.getID())

                if(col == length - 1):
                    if(fastSearchNextTile(row+1, 0, tiles, length, grid, visited)):
                        return True
                else:
                    if(fastSearchNextTile(row, col+1, tiles, length, grid, visited)):
                        return True

                visited.remove(tile.getID())
        return False


#Joins tiles arrangements to create the final image
def createTilesImage(grid):
    image = []
    numberOfHastags = 0
    h = len(grid[0][0].getFinalDrawing())
    w = len(grid[0][0].getFinalDrawing()[0])
    for row in grid:
        for i in range(h):
            s = ''
            for tile in row:
                s += tile.getFinalDrawing()[i]
            image.append(s) 
            numberOfHastags += s.count('#')

    return image,numberOfHastags

#Searches for the monsters in the image (original, rotated and flipped)
def searchMonsters(monster_coordinates, image):
    numMonsters = 0
    for _ in range(2):
        for _ in range(4):            
            for i,line in enumerate(image):
                for j,l in enumerate(line):
                    if l == '#':
                        isMonster = True
                        for (x,y) in monster_coordinates:
                            xToLook = i + x
                            yToLook = j + y
                            if(xToLook in range(len(image)) and yToLook in range(len(image[0]))):
                                if(image[xToLook][yToLook] != '#'):
                                    isMonster = False
                                    break
                            else:
                                isMonster = False
                                break

                        if(isMonster):
                            numMonsters += 1

            if(numMonsters > 0):
                return numMonsters

            image = rotate(image)
        image = flip(image)
    return 0


#Gets monster's hastags coordinates using the first # as origin
# It returns the coordinates of all the # positions from the origin,
# except for the coordinates of the origin
def getMonsterCoordinates(monster):
    coordinates = []
    iFirstHastag = -1
    jFirstHastag = -1
    for i,line in enumerate(monster):
        jFirstHastag = line.find('#')
        if jFirstHastag != -1: 
            iFirstHastag = i
            break

    for i,line in enumerate(monster):
        for j in range(len(line)):
            if line[j] == '#':
                coordinates.append((i-iFirstHastag,j-jFirstHastag))
    
    coordinates.remove((0,0))
    return coordinates


#Part 2 
def p20_2(fileName):
    with open(fileName, 'r')  as f:
        lines = [line.strip() for line in f]
        tiles,length = getAllPossibleTiles(parseInput(lines))
        
        length = math.ceil(math.sqrt(length))
        grid = [[Tile(0,[]) for x in range(length)] for y in range(length)]

        fastSearchNextTile(0,0,tiles,length,grid,[])

        for row in grid:
            for tile in row:
                tile.removeBorders()

        monster = ['                  # ',
                   '#    ##    ##    ###',
                   ' #  #  #  #  #  #   ']

        monster_coordinates = getMonsterCoordinates(monster)
        monsterHastags = len(monster_coordinates)+1

        image, numHastags = createTilesImage(grid)

        numMonsters = searchMonsters(monster_coordinates, image)
        return numHastags - monsterHastags*numMonsters


#Main
result = p20('input.txt')   
print("P20 ->", result)

result = p20_2('input.txt')   
print("P20_2 ->", result)
