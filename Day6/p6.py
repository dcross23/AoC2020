from string import ascii_lowercase

#Problem 6 solution (part 1)
def createJoinedGroupsAsList(lines):
    groups = ''
    for l in lines:
        if l != '':
            groups += l
        else:
            groups += ' '
    return groups.split(' ')
  
def countYesResponses(group):
    uniqueLetters=[]
    for c in group:
        if c not in uniqueLetters:
            uniqueLetters.append(c)
            
    return len(uniqueLetters)

#1rst part solution  
def p6(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        
        groups = createJoinedGroupsAsList(lines)
        counter = 0
        for group in groups:
            counter  += countYesResponses(group)
            
        return counter
        
#Problem 6 solution (part 2)    
def createSeparateGroupsAsLists(lines):
    groups = []
    newGroup = []
    for l in lines:
        if l != '':
            newGroup.append(l)
        else:
            groups.append(newGroup)
            newGroup = []

    groups.append(newGroup)
    return groups

def countAllYesResponses(group):
    questionsAllYes = ''   
    
    for car in group[0]:
        carIsInPersonResp = True
        for person in group:
            if car not in person:
                carIsInPersonResp = False
                break
                
        if carIsInPersonResp and car not in questionsAllYes:
            questionsAllYes += car
            
    return len(questionsAllYes)
    
#2nd part solution 
def p6_2(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]
        groups = createSeparateGroupsAsLists(lines)
        
        counter = 0
        for group in groups:
            counter  += countAllYesResponses(group)
            
        return counter     
        
#Main
result = p6('input.txt')
print("P6 ->", result)

result = p6_2('input.txt')
print("P6_2 ->", result)