#Problem 25 solution (part 1)
def processPublicKey(publicKey):
    neededLoopSize = 0
    while pow(7, neededLoopSize, 20201227) != publicKey:
        neededLoopSize += 1
    return neededLoopSize

#1rst part "main"
def p25(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        cardPublicKey = int(lines[0].strip())
        doorPublicKey = int(lines[1].strip())

        cardLoopSize = processPublicKey(cardPublicKey)
        #doorLoopSize = processPublicKey(doorPublicKey)
        
        return pow(doorPublicKey, cardLoopSize, 20201227)


#Problem 25 solution (part 2)
#There is not 2nd part -> "HAPPY CHRISTMAS :D"

#Main
result = p25('input.txt')   
print("P25 ->", result)

