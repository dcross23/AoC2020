import itertools

#Problem 2 solution (part 1)
def p2(fileName):
    with open(fileName, 'r') as f:
        counter = 0
        for line in f:
            li = line.replace(':','').strip().split(" ")
            m,M = [int(x) for x in li[0].strip().split("-")]
            n = li[2].count(li[1])
            if m <= n <= M:
                counter = counter + 1            

    return counter


#Problem 2 solution (part 2)
def p2_2(fileName):
    with open(fileName, 'r') as f:
        counter = 0
        for line in f:
            l = line.replace(':','').strip().split(" ")
            pos1,pos2 = [int(x) for x in l[0].strip().split("-")]
            car1 = l[2][pos1-1]
            car2 = l[2][pos2-1]
            
            if (car1==l[1]) ^ (car2==l[1]):
                counter = counter + 1            

    return counter
           
    
#Main
result = p2('input.txt')
print("P2 ->",result)

result = p2_2('input.txt')
print("P2_2 ->",result)

    
