#Problem 16 solution (part 1) 
#Gets the ranges (without getting the names) and gets the nearby tickets
def parseInput1(lines):
    ranges,nearby_tickets = [],[]
    scanningNearbyTickets = False
    scanningRanges = True
    
    for l in lines:
        if 'your ticket' in l:
            scanningRanges = False
            continue 
            
        if scanningRanges == True:
            newRange = l.split(':')[1].strip().split(' or ')
            newRange = [l.split('-') for l in newRange]
            ranges.append(newRange)

        elif scanningNearbyTickets == True:
            nearby_tickets.append([int(x) for x in l.split(',')]) 

        if 'nearby tickets' in l:
            scanningNearbyTickets = True
            continue 

    return ranges, nearby_tickets


#1rst part "main" 
def p16(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f if l != '\n']
        ranges,nearby_tickets = parseInput1(lines)

        result,validTickets = 0, []
        for ticket in nearby_tickets:
            validTicket = True
            for value in ticket:
                validNumber = False
                for r in ranges:
                    range1 = (int(r[0][0]), int(r[0][1]))
                    range2 = (int(r[1][0]), int(r[1][1]))
                    if range1[0]<=int(value)<=range1[1] or range2[0]<=int(value)<=range2[1]:
                        validNumber = True
                        break

                if not validNumber:
                    result += int(value)
                    validTicket = False
                    break
            if validTicket:
                validTickets.append(ticket)

        return result, validTickets


#Problem 16 solution (part 2)
# 1rst attempt of creating a backtracking function. It works for examples, 
#   but it seems to be too slow for the input (I just wanted to keep it ;D)
#
#def getValidValidatorsBacktracking( possibilities, validators):
#    if len(possibilities) == 0:
#        return []
#    
#    else:
#        possibility = possibilities[0]
#        for validator in possibility[1]:
#            isInValidators = False
#            for v in validators:
#                if validator in v:
#                    isInValidators = True
#
#            if not isInValidators:
#                validators.append([possibility[0], validator])
#
#                nextValidators = getValidValidatorsBacktracking(possibilities[1:], validators)
#                if nextValidators != None:
#                    return []
#                else:
#                    validators.remove([possibility[0], validator])
#        return None   

#

#Gets the ranges (with the names) and gets my ticket 
def parseInput2(lines):
    ranges = {}
    for i,l in enumerate(lines):
        if l.startswith('your ticket'):
            myTicket = lines[i+1].split(',')
            break

        else:
            nameAndRanges = l.split(':')
            newRange = nameAndRanges[1].strip().split(' or ')
            newRange = [l.split('-') for l in newRange]
            ranges[nameAndRanges[0]] = newRange

    return ranges, myTicket    

#Returns the valid ranges (possibilities) for each column (thats why we work with the
# the transposed matrix, to have columns as rows) in the valid tickets. 
#With the example we get: 
#   [ [0,['row']] , [1,['class','row']], [2,['class', 'row', 'seat']] ]
#This means, for column 0 (element 0 in valid tickets), the only range accepted is 
# the 'row' one, for column 1 are 'class' and 'row' and what ever.
#This list of possibilities is returned
def getPossibilities(nameAndRanges, transposed):
    possibilities = []
    for numCol,inputColumn in enumerate(transposed):
        iCpossibilities = [name for name,ranges in nameAndRanges.items()]
        for element in inputColumn:
            for name,ranges in nameAndRanges.items():
                range1 = (int(ranges[0][0]), int(ranges[0][1]))
                range2 = (int(ranges[1][0]), int(ranges[1][1]))
                if not (range1[0]<=element<=range1[1] or range2[0]<=element<=range2[1]):
                    if name in iCpossibilities:
                        iCpossibilities.remove(name)

        possibilities.append([numCol, iCpossibilities])
    return possibilities

#Using the possibilies gotten with 'getPossibilities' function, we search 
# for a column with only one possible range. This is added to the solution as
# [columnX, ['rangeName']]
#Then, the rangeName given as solution to columnX is removed from all the possibilies
# of all the other columns and then the process is repeated recursively because there will
# be always one column with only one possibility.
def getValidValidators(possibilities, validators):
    if len(possibilities) == 0:
        return []

    else:
        possibility = None
        for p in possibilities:
            if len(p[1]) == 1:
                possibility = p
                break

        if possibility != None:
            validators.append(possibility)
            possibilities.remove(possibility)
            for p in possibilities:
                p[1].remove(possibility[1][0])

            getValidValidators(possibilities, validators)


#2nd part "main"
def p16_2(fileName, validTickets):
    with open(fileName, 'r') as f:
            lines = [l.strip() for l in f if l != '\n']
            nameAndRanges, myTicket = parseInput2(lines) 
            transposedMatrix = [[ validTickets[row][col] for row in range(0,len(validTickets)) ] for col in range(0,len(validTickets[0])) ]
            
            possibilities = getPossibilities(nameAndRanges, transposedMatrix)

            validators = []
            getValidValidators(possibilities, validators)

            departureValidators = [v for v in validators if v[1][0].startswith('departure')]            
            result = 1
            for dv in departureValidators:
                result *= int(myTicket[dv[0]])
            return result

            

#Main
fileName = 'input.txt'
result, validTickets = p16(fileName)   
print("P16 ->", result)

result = p16_2(fileName, validTickets)
print("P16_2 ->", result)