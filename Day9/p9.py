#Problem 9 solution (part 1)  
def p9(fileName, preamble):
    with open(fileName, 'r') as f:
        lines = [int(line.strip()) for line in f]

        for i,l in enumerate(lines):
            if i >= preamble:
                preambleNums = lines[i-preamble:i]
                isSumFlag = False
                for n in preambleNums:
                    if l-n in preambleNums:
                        isSumFlag = True

                if not isSumFlag:
                    return l         


#Problem 9 solution (part 2) 
def findSetOfNumbers(number, lines):
    for i,l in enumerate(lines):
            solution = [l]
            accumulator = l

            if accumulator < number:
                for n in lines[i+1:]:
                    if accumulator + n > number:
                        break

                    else:
                        solution.append(n)
                        if accumulator + n == number:
                            return solution
                        else:
                            accumulator += n                      


def p9_2(fileName, number):
    with open(fileName, 'r') as f:
        lines = [int(line.strip()) for line in f if int(line.strip()) != number]
        setOfNumbers = findSetOfNumbers(number, lines)
        return max(setOfNumbers) + min(setOfNumbers)   


             
#Main
result = p9('input.txt',25)
print("P9 ->", result)

result = p9_2('input.txt',result)
print("P9_2 ->", result)