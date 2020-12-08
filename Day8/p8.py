#Problem 8 solution (part 1)  
def run(lines):
    accumulator = 0
    currentLine = 0
    visitedLines = []
    while 0<=currentLine<len(lines) and currentLine not in visitedLines:
        visitedLines.append(currentLine)
        opcode = lines[currentLine].split(' ')

        if opcode[0] == 'nop':
            currentLine += 1

        elif opcode[0] == 'acc':
            accumulator += int(opcode[1])
            currentLine += 1

        elif opcode[0] == 'jmp':
            currentLine += int(opcode[1]) 
    return accumulator


def p8(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        return run(lines)


#Problem 8 solution (part 2)
def run2(lines):
    accumulator = 0
    currentLine = 0
    visitedLines = []
    while 0<=currentLine:
        visitedLines.append(currentLine)
        opcode = lines[currentLine].split(' ')

        if opcode[0] == 'nop':
            currentLine += 1

        elif opcode[0] == 'acc':
            accumulator += int(opcode[1])
            currentLine += 1

        elif opcode[0] == 'jmp':
            currentLine += int(opcode[1])   

        if currentLine == len(lines):
            return ("ok", accumulator)
        elif currentLine in visitedLines:
            return ("no valid", accumulator)

def p8_2(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]

        for i,l in enumerate(lines):
            modifiedLines = lines.copy()

            if l.split(' ')[0] == 'nop':
                modifiedLines[i] = 'jmp ' + l.split(' ')[1]  

            elif l.split(' ')[0] == 'jmp':
                modifiedLines[i] = 'nop ' + l.split(' ')[1]   

            else:
                continue

            result = run2(modifiedLines)
            if result[0] == 'ok':
                return result[1]


#Main
result = p8('input.txt')
print("P8 ->", result)

result = p8_2('input.txt')
print("P8_2 ->", result)