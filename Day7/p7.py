#Problem 7 solution (part 1)  
def prepareGraph(lines):
    graph = [line.split(' contain') for line in lines]
    for g in graph:
        g[0] = g[0][:g[0].index(' bags')]
        g[1] = g[1].strip()

    return graph

def getBagsThatContain(graph, color):
    bagsThatContainsColor = [ g for g in graph if color in g[1]]

    visitedColors = []
    if not bagsThatContainsColor:
        return []

    else:
        allColors = [ line[0] for line in bagsThatContainsColor ] 
        notVisitedColors = [c for c in allColors if c not in visitedColors]

        #For each unvisited colors, it visits them and looks for the
        # bags that contains that color recursively, so it will look for
        # the bags that contain the bags the contain... the bag that contains
        # the color searched in first place (shiny gold)
        for c in notVisitedColors:
            visitedColors.append(c)
            visitedColors += getBagsThatContain(graph, c)

        #Remove duplicate colors from the list and return them
        return list(dict.fromkeys(visitedColors))
    
#1rst part solution  
def p7(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        graph = prepareGraph(lines)
        bagsThatCanContainShinyGold = getBagsThatContain(graph, 'shiny gold')
        return len(bagsThatCanContainShinyGold)
            
     

#Problem 7 solution (part 2)
def bagsContained(graph,color):
    colorLine = [g for g in graph if g[0] == color][0]
    containedBags = [ cl.strip().replace('.','') for cl in colorLine[1].split(',') ]

    counter = 1
    for bag in containedBags:
        splitedBag = bag.split(' ')
        if splitedBag[0] != 'no':
            bagsNum   = int(splitedBag[0])
            bagsColor = splitedBag[1] + ' ' + splitedBag[2]
            counter += (bagsNum * bagsContained(graph, bagsColor))

    return counter

def p7_2(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        graph = prepareGraph(lines)

        #-1 because we dont want to count the shiny gold bag
        numBags = bagsContained(graph, 'shiny gold') - 1
        return numBags

#Main
result = p7('input.txt')
print("P7 ->", result)

result = p7_2('input.txt')
print("P7_2 ->", result)