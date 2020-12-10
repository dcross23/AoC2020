#Problem 10 solution (part 1)  
def p10(fileName):
    with open(fileName, 'r') as f:
        lines = sorted([int(line.strip()) for line in f])
        lines = [0] + lines #we add the 0 that is the start
        diff1jolt = 0
        diff3jolts = 0
        
        for i in range(len(lines) - 1):
            diffjolts = lines[i+1] - lines[i]
            if(diffjolts == 1): 
                diff1jolt += 1

            elif(diffjolts == 3):
                diff3jolts += 1

        #+1 cause we have to consider our devide internal adapter
        return diff1jolt * (diff3jolts+1) 


#Problem 10 solution (part 2)  
#CombforNum stores how many combinations are valid for a number
#  (try to avoid recalculations)
def diffArrangements(pos, lines, CombforNum):
    #If we reached the end, we return 1 (1 new combination)
    if pos == len(lines) - 1:
        return 1

    #If we have not reached the end but we already know how many combinations are valid
    #  for that pos, we just get the number of combinatios from the dictionary
    elif pos in CombforNum:
        return CombforNum[pos]

    #If we have not reached the end and we have not calculated previously how many
    #  combinations for pos are valid, we calculate and register them
    else:
        combinationsForPos = 0
        for nextNum in range(pos+1, len(lines)):
            if lines[nextNum] - lines[pos] <= 3:
                combinationsForPos += diffArrangements(nextNum, lines, CombforNum)

        CombforNum[pos] = combinationsForPos
        return combinationsForPos


def p10_2(fileName):
    with open(fileName, 'r') as f:
        lines = sorted([int(line.strip()) for line in f])
        lines = [0] + lines
        result = diffArrangements(0, lines, {})
        return result
        


#Main
result = p10('input.txt')
print("P10 ->", result)

result = p10_2('input.txt')
print("P10_2 ->", result)