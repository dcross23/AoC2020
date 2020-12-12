#Problem 12 solution (part 1) 
#Moves the boat a certain distance(num) according to its direction 
def incDirectionCounter(direction, num):
    if direction == 'N':
        return num, 0 
    elif direction == 'E':
        return 0,num
    elif direction == 'S':
        return -num, 0
    elif direction == 'W':
        return 0, -num

#Changes the direction right(R) or left(L) by an ammount of degrees (num)
def changeDirection(direction, action, num):
    directions = ['N','E','S','W']
    dirIndex = directions.index(direction)
    changes = int(num / 90)

    if action == 'R':
        dirIndex = (dirIndex + changes) % 4
    elif action == 'L':
        dirIndex = (dirIndex - changes) % 4

    return directions[dirIndex]

#1rst part main loop
def p12(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f]    
        ns, ew = 0, 0
        direction = 'E'  
        
        for movement in lines:
            action, num = movement[:1], int(movement[1:])

            if action == 'F':
                nsInc, ewInc = incDirectionCounter(direction, num)
                ns += nsInc
                ew += ewInc

            elif action == 'N':
                ns += num
            elif action == 'S':
                ns -= num
            elif action == 'E':
                ew += num
            elif action == 'W':
                ew -= num

            elif action == 'R' or action == 'L':
                direction = changeDirection(direction, action, num)

        return abs(ns) + abs(ew)




#Problem 12 solution (part 2)  
#Moves the boat by the direction of the waypoint and a multiplier (number close to action)
def incDirByWaypoint(waypoint, num):
    nsInc, ewInc = 0,0
    for direction in waypoint:
        if direction[1] == 'N':
            nsInc += int(direction[0]) * num
            ewInc += 0
        elif direction[1] == 'E':
            nsInc += 0
            ewInc += int(direction[0]) * num
        elif direction[1] == 'S':
            nsInc -= int(direction[0]) * num
            ewInc += 0
        elif direction[1] == 'W':
            nsInc += 0
            ewInc -= int(direction[0]) * num
    return nsInc, ewInc

#Changes de direction of both coodinates of the waypoint
def changeWaypointDirection(waypoint, action, num):
    for direction in waypoint:
        direction[1] = changeDirection(direction[1], action, num)
    return waypoint

#Gets the coodinate of the waypoint that corresponds to the action or the opposite
# coordinate of the action and returns it with the index where the coordinate
# is located in the waypoint (0 or 1)
def getCorrectOrOpositeDirection(waypoint, action):
    if(action == 'N'):
        opposite = 'S'

    elif(action == 'S'):
        opposite = 'N'

    elif(action == 'E'):
        opposite = 'W'

    elif(action == 'W'):
        opposite = 'E'

    for i, direction in enumerate(waypoint):
        if direction[1] == action:
            return i,action
        elif direction[1] == opposite:
            return i,opposite

#2nd part main loop
def p12_2(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f]  
        ns, ew = 0, 0
        waypoint = [[10,'E'], [1,'N']]

        for movement in lines:
            action, num = movement[:1], int(movement[1:])

            if action == 'F':
                nsInc, ewInc = incDirByWaypoint(waypoint, num)
                ns += nsInc
                ew += ewInc

            elif action in ['N','S','E','W'] :
                index, actVSdir = getCorrectOrOpositeDirection(waypoint, action)
                if actVSdir == action:
                    waypoint[index][0] += num
                else:
                    waypoint[index][0] -= num


            elif action == 'R' or action == 'L':
                waypoint = changeWaypointDirection(waypoint, action, num)

        return abs(ns) + abs(ew)



#Main
result = p12('input.txt')   
print("P12 ->", result)

result = p12_2('input.txt')   
print("P12_2 ->", result)