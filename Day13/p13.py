from functools import reduce

#Problem 13 solution (part 1) 
def p13(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f]    
        timestamp = int(lines[0])
        busesIDs = [int(bus) for bus in lines[1].split(',') if bus != 'x']
        
        currentTime = timestamp
        while True:
            for bus in busesIDs:
                if currentTime % bus == 0:
                    return ((currentTime-timestamp) * bus)

            currentTime += 1


#Problem 13 solution (part 1) 

#Brutal force solution (works with example but for input is tooo slow)
#def brutalForceSolution(lines):
#    t = int(lines[0])
#    busesIDs = [(i,bus) for i,bus in enumerate(lines[1].split(',')) if b != 'x']
#    while True:
#            finded = True
#            for bus in busesIDs:
#                if (t+bus[1]) % bus[0] != 0:
#                    finded = False
#                    break
#
#           if finded == True:
#                return t
#
#            t+=1

#Chinese remainder theorem solution
# credits to dylan-codesYT for chinese remainder theorem algorithm in python ->
# -> https://github.com/dylan-codesYT/AdventOfCode2020/blob/master/day13.py
def mul_inv(a, b):
    # find some x such that (a*x) % b == 1
    if b == 1:
        return 1
    else:
        a = a % b
        for x in range(1, b):
            if (a*x) % b == 1:
                return x

def chinese_remainder(buses, N):
    sol = 0
    for i,k in buses:
        p = N // k
        sol += (mul_inv(p,k) * p * i)

    return sol % N

#2nd part "main"
def p13_2(fileName):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f]   
        #return brutalForceSolution(lines)

        t = int(lines[0])
        busesIDs = [bus for bus in lines[1].split(',')]

        # n busses, each one at index i departs at a time t+i
        # t+i % k == 0    |->     t % k == -i    |-> 
        # t % k = k-i     |->      index = (k - (i%k)) % k
        buses = []
        N = 1
        for i,bus in enumerate(busesIDs):
            if bus!='x':
                bus = int(bus)
                i %= bus
                buses.append(((bus-i)%bus, bus))
                N *= bus

        return chinese_remainder(buses, N)


#Main
result = p13('input.txt')   
print("P13 ->", result)

result = p13_2('input.txt') 
print("P13_2 ->", result)