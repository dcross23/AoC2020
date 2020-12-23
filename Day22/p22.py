#Problem 22 solution (part 1) 
def newRound(player1, player2):
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    elif p1 < p2:
        player2.append(p2)
        player2.append(p1)

    return player1, player2

#1rst part main 
def p22(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]

        player1 = [int(x) for x in lines[1:lines.index('')]]
        player2 = [int(x) for x in lines[lines.index('')+2:]]

        while player1!=[] and player2!=[]:
            player1, player2 = newRound(player1, player2)

        winner = [player1 if player1 != [] else player2][0]
        
        result = 0
        for i,x in enumerate(reversed(winner)):
            result += (x * (i+1))
        return result




#Problem 22 solution (part 2) 
def recursiveCombat(player1, player2, rounds):
    while player1!=[] and player2!=[]:
        if [player1, player2] in rounds:
            return 'player1'

        else:
            rounds.append([player1.copy(), player2.copy()])
            p1 = player1.pop(0)
            p2 = player2.pop(0)
            
            if len(player1) >= p1 and len(player2) >= p2:
                subWinner = recursiveCombat(player1.copy()[:p1], player2.copy()[:p2], [])
                if subWinner == 'player1':
                    player1.append(p1)
                    player1.append(p2)
                elif subWinner == 'player2':
                    player2.append(p2)
                    player2.append(p1)

            else:
                if p1 > p2:
                    player1.append(p1)
                    player1.append(p2)

                elif p1 < p2:
                    player2.append(p2)
                    player2.append(p1)

    return ['player1' if player1 != [] else 'player2'][0]


#2nd part "main"
def p22_2(fileName):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]

        player1 = [int(x) for x in lines[1:lines.index('')]]
        player2 = [int(x) for x in lines[lines.index('')+2:]]
        
        winner = recursiveCombat(player1, player2, [])
        if winner == 'player1':
            winner = player1
        else:
            winner = player2

        result = 0
        for i,x in enumerate(reversed(winner)):
            result += (x * (i+1))
        return result



#Main
result = p22('input.txt')   
print("P22 ->", result)

result = p22_2('input.txt')   
print("P22_2 ->", result)
