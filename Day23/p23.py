#Problem 23 solution (part 1) 
def p23(fileName,movements):
    with open(fileName, 'r') as f:
        cups = [line.strip() for line in f][0]
        currentCup = (0,cups[0])
        
        #Game loop
        for i in range(1,movements+1):
            #Gets the 3 next cups (clockwise) and remove them from cups
            closeCups = ''
            for j in range(1,4):
                pos = (currentCup[0] + j)%len(cups)
                closeCups += cups[pos]

            for cc in closeCups:
                cups = cups.replace(cc,'')

            #Get destination cup
            destinationCup = int(currentCup[1])-1

            while destinationCup<int(min(cups)) or str(destinationCup) in closeCups:
                destinationCup = (destinationCup - 1)
                if destinationCup < int(min(cups)):
                    destinationCup  = int(max(cups))

            dCIndex = cups.find(str(destinationCup))

            #Add close cups immediatly clockwise the destination cup
            cups = cups[:dCIndex+1] + closeCups + cups[dCIndex+1:]
            while cups.find(str(currentCup[1])) != currentCup[0]:
                cups = cups[1:] + cups[0]

            ccIndex = (currentCup[0]+1)%len(cups)
            currentCup = (ccIndex, cups[ccIndex])


        #Get cups ordered clockwise starting for cup labeled 1
        counter = cups.find('1') + 1
        result = ''
        while counter != cups.find('1'):
            result += cups[counter]
            counter = (counter+1)%len(cups)

        return result


#Problem 23 solution (part 2)
#TODO : part 2 (refactor part 1 to lists instead of strings)

#Main
result = p23('input.txt', 100)   
print("P23 ->", result)

