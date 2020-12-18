#Loads the first given layer in the input
def getFirstLayer(f):
    lines = [l.strip() for l in f]
    onCubes = set()
    for x,l in enumerate(lines):
        for y,car in enumerate(l):
            if car == '#':
                    onCubes.add((x,y,0,0))

    return onCubes, len(lines)

#Get the active neightboors of a (x,y,z) position
# For part 2, adds a new dimension t
def getOnNeightboors(onCubes,x,y,z,t):
    neightboors = 0
    for xPos in [-1,0,1]:
        for yPos in [-1,0,1]:
            for zPos in [-1,0,1]:
                #Part 1
                if t == None:
                    if not (xPos==0 and yPos==0 and zPos==0):
                        if (x+xPos, y+yPos, z+zPos,0) in onCubes:
                            neightboors += 1
                #Part2
                else:
                    for tPos in [-1,0,1]:   
                        if not (xPos==0 and yPos==0 and zPos==0 and tPos==0):
                            if (x+xPos, y+yPos, z+zPos, t+tPos) in onCubes:
                                neightboors += 1 
    return neightboors

#Returns the range of possible cubes that can change for each dimension.
# This is, if we have dimension 1 (x) in range -1 to 1 (this is -1,0,1), the possible 
# cubes that can change the state are in range -2 to 2
def rangeOf(i, onCubes):
    return range(min(indexes[i] for indexes in onCubes)-1, max(indexes[i] for indexes in onCubes)+2)

#With the given active cubes, it calculates the next active cubes 
# The difference between part 1 and part 2 is the 4rth dimension, which is always
# 0 in the 1rst part while in 2nd part may vary
def newStep(onCubes, hw, part):
    newOnCubes = set()
    for x in rangeOf(0,onCubes):
        for y in rangeOf(1,onCubes):
            for z in rangeOf(2,onCubes):
                if part == 1:
                    activeNeighbors = getOnNeightboors(onCubes,x,y,z,None)
                    if (x,y,z,0) not in onCubes and activeNeighbors==3:
                        newOnCubes.add((x,y,z,0))

                    if (x,y,z,0) in onCubes and activeNeighbors in [2,3]:
                        newOnCubes.add((x,y,z,0))

                else:
                    for t in rangeOf(3, onCubes):
                        activeNeighbors = getOnNeightboors(onCubes,x,y,z,t)
                        if (x,y,z,t) not in onCubes and activeNeighbors==3:
                            newOnCubes.add((x,y,z,t))

                        if (x,y,z,t) in onCubes and activeNeighbors in [2,3]:
                            newOnCubes.add((x,y,z,t))

    return newOnCubes



#Problem 17 solution (part 1) 
def p17(fileName,part):
    with open(fileName, 'r') as f:
        onCubes,hw = getFirstLayer(f)
        for step in range(6):
            onCubes = newStep(onCubes,hw, part)

        return len(onCubes)       

        
#Problem 17 solution (part 2) 
def p17_2(fileName, part):
    return p17(fileName,part)


#Main
result = p17('input.txt',1)   
print("P17 ->", result)

result = p17_2('input.txt',2)   
print("P17_2 ->", result)