#Problem 24 solution (part 1) 

#Given a tile (from input), it return its coordinates
# using "Cube coordinates"
def getTileCoordinates(tile):
    x,y,z = 0,0,0
    while tile != '':
        if tile.startswith('e'):
            x += 1
            y -= 1
            tile = tile[1:]

        elif tile.startswith('w'):
            x -= 1
            y += 1
            tile = tile[1:]

        elif tile.startswith('ne'):
            x += 1
            z -= 1
            tile = tile[2:]

        elif tile.startswith('nw'):
            y += 1
            z -= 1
            tile = tile[2:]

        elif tile.startswith('se'):
            y -= 1
            z += 1
            tile = tile[2:]

        elif tile.startswith('sw'):
            x -= 1
            z += 1
            tile = tile[2:]
    return (x,y,z)

#1rst part "main"
def p24(fileName):
    with open(fileName, 'r') as f:
        tiles = [line.strip() for line in f]
        blackTiles = []

        for tile in tiles:
            coordinates = getTileCoordinates(tile)

            #If that tile is already black, we flipped to white 
            #  (remove from black tiles list).
            #If that tile is white, we flip it and store it 
            # as a black tile.
            if coordinates in blackTiles:
                blackTiles.remove(coordinates)
            else:
                blackTiles.append(coordinates)    

        return blackTiles   


#Problem 24 solution (part 2)

#Get all the tiles that have to be checked. That tiles are the ones
# on the flipped tiles list and its neighboors
def getTilesToCheck(flippedTiles):
    neighboors = [(1,-1,0),(-1,1,0),(1,0,-1),(0,1,-1),(0,-1,1),(-1,0,1)]

    tilesToCheck = set()
    for (x,y,z) in flippedTiles:
        tilesToCheck.add((x,y,z))
        for (nx,ny,nz) in neighboors:
            tilesToCheck.add((x+nx, y+ny, z+nz))

    return tilesToCheck

#Given a tile, gets the number of neighboor tiles that are black
def getBlackNeighboors(tile, flippedTiles):
    (x,y,z) = tile
    neighboors = [(1,-1,0),(-1,1,0),(1,0,-1),(0,1,-1),(0,-1,1),(-1,0,1)]
    
    blackNeighboors = 0
    for (nx,ny,nz) in neighboors:
        if (x+nx, y+ny, z+nz) in flippedTiles:
            blackNeighboors += 1
    return blackNeighboors

#2nd part "main"
def p24_2(flippedTiles):
    for _ in range(100):
        newFlipped = set()
        tilesToCheck = getTilesToCheck(flippedTiles)

        for tile in tilesToCheck:
            blackNeighboors = getBlackNeighboors(tile, flippedTiles)
            if tile in flippedTiles and blackNeighboors in [1,2]:
                newFlipped.add(tile)

            if tile not in flippedTiles and blackNeighboors == 2:
                newFlipped.add(tile)

        flippedTiles = newFlipped

    return len(flippedTiles)


#Main
flippedTiles = p24('input.txt')   
print("P24 ->", len(flippedTiles))

result = p24_2(flippedTiles)  
print("P24_2 ->", result)
