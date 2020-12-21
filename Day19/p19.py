#Problem 19 solution (part 1)
def parseInput(lines):
    rules, messages = {},[]
    gettingRules = True
    for l in lines:
        if l =='':
            gettingRules = False
            continue

        if gettingRules == True:
            splitRule = l.split(':')
            splitRule[1] = splitRule[1].strip()
            if '"' in splitRule[1]:
                rules[splitRule[0]] = splitRule[1][1:-1]
            else:
                temp = splitRule[1].split(' | ')
                rules[splitRule[0]] = []
                for r in temp:
                    rules[splitRule[0]].append(r.split(' '))
        
        else:
            messages.append(l)

    return rules, messages

#Gets all combinations from elements of 2 lists
# Example -> ['a','b'] and ['aa','ab'] --> ['aaa','aab','baa','bab']
def combine(list1, list2):
    combined = []
    for s1 in list1:
        for s2 in list2:
            combined.append(s2+s1)
    return combined

#Gets all possible combinations from a given rule
#Using dinamic programming to improve performances, it stores the visited 
# rules in case it has to repeat that rule.
def getCombinations(rule, allRules, visitedRules):
    rulesFromRule = allRules[rule]
    if type(rulesFromRule) == str:
        return [rulesFromRule]
    
    elif rule in visitedRules:
        return visitedRules[rule]

    else:
        allCombinations = []
        for subRule in rulesFromRule:
            newComb = []
            for nextR in subRule:
                diferentComb = getCombinations(nextR, allRules,visitedRules)

                if len(newComb) == 0:
                    newComb = diferentComb.copy()
                else:
                    newComb = combine(diferentComb, newComb)

            allCombinations += newComb  

        visitedRules[rule] = allCombinations      
        return allCombinations


#1rst part "main"
def p19(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]  
        allRules, messages = parseInput(lines)
        allCombinations = getCombinations('0', allRules,{})

        #Removes repeated combinations in case there are
        allCombinations = list(dict.fromkeys(allCombinations))

        numCorrectMessages = len([m for m in messages if m in allCombinations])
        return numCorrectMessages




#Problem 19 solution (part 2) 
#Too dificult for me :D
#This part is a slightly modified solution from dylan-codesYT
# (https://github.com/dylan-codesYT/AdventOfCode2020/blob/master/day19.py)
def p19_2(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f] 
        allRules, messages = parseInput(lines)

        r42 = getCombinations('42', allRules, {})
        r31 = getCombinations('31', allRules, {})
        chunkSize = len(r42[0])
        count = 0
        for msg in messages:
            chunks42 = [False for _ in range(len(msg)//chunkSize)]
            chunks31 = [False for _ in range(len(msg)//chunkSize)]

            # determine which chunks come from which rules
            currChunk = 0
            for i in range(0, len(msg), chunkSize):
                if msg[i:i+chunkSize] in r42:
                    chunks42[currChunk] = True
                if msg[i:i+chunkSize] in r31:
                    chunks31[currChunk] = True
                currChunk += 1
            # does this message match the rules?
            count42, count31 = 0,0
            currChunk = 0
            if chunks42[currChunk] == True:
                count42 += 1
                currChunk +=1
                while currChunk < len(chunks42) and chunks42[currChunk]:
                    count42 += 1
                    currChunk += 1
                while currChunk < len(chunks31) and chunks31[currChunk]:
                    count31 += 1
                    currChunk += 1
                if currChunk == len(chunks31) and 0 < count31 < count42:
                    count += 1

        return count


#Main
result = p19('input.txt')   
print("P19 ->", result)

result = p19_2('input.txt')
print("P19_2 ->", result)