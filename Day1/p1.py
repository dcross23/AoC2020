import itertools

#Problem 1 solution (part 1)
def p1(fileName):
    with open(fileName, 'r') as f:
        input_file = [line.rstrip() for line in f]
        for i in input_file:
            i = int(i)
            sub = 2020 - i
            if str(sub) in input_file:
                return sub*i

    return -1

#Problem 1 solution (part 2)
def p1_2(fileName):
    with open(fileName, 'r') as f:
        input_file = [line.rstrip() for line in f]
        perm = itertools.permutations(input_file, 3)
        for a,b,c in perm:
            if int(a)+int(b)+int(c) == 2020:
                return int(a)*int(b)*int(c)

    return -1
            
    
#Main
result = p1('input.txt')
if result != -1:
    print("P1_2 ->",result)
    
result2 = p1_2('input.txt')
if result2 != -1:
    print("P1_2 ->",result2)
    
