#Algorithm that recreates the game
def sequence(lines, lastTurn):
    numAppearances = {int(i):[j+1,j+1] for j,i in enumerate(lines)}
    turn = len(numAppearances)+1
    lastNumber = int(lines[-1])

    while turn <= lastTurn:
        lastNumberAppearances = numAppearances[lastNumber]
        nextNumber = lastNumberAppearances[1] - lastNumberAppearances[0]

        if nextNumber in numAppearances:
            numAppearances[nextNumber][0] = numAppearances[nextNumber][1]
            numAppearances[nextNumber][1] = turn
        else:
            numAppearances[nextNumber] = [turn, turn]

        lastNumber = nextNumber
        turn += 1

    return lastNumber



#Problem 15 solution (part 1) 
def p15(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f][0].split(',')
        return sequence(lines, 2020)


#Problem 15 solution (part 2)
def p15_2(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f][0].split(',')
        return sequence(lines, 30000000)

#Just changes lastTurn to 30000000. Seems like it will not work, but waiting
# a little it just gives you the answer (slow but gives it).
#For example, for all test the time spended was -> Ran 2 tests in 175.063s
#Is slow but works ;D
#
#AThe best solution is using "Van Eck Sequence"

#Main
result = p15('input.txt')   
print("P15 ->", result)

result = p15_2('input.txt')   
print("P15_2 ->", result)

