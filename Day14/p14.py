#Problem 14 solution (part 1) 
#Decoder for part 1
def decoderV1(lines):
    mask = None   
    memory = {}
    for l in lines:
        if(l.startswith("mask")):
            # l = ['mask ', ' XX10X...']
            # l[1].strip() -> 'XX10X...'
            mask = l.split('=')[1].strip() 
        
        else:
            #memPos = mem[153415] 
            #memPos.split('[') = ['mem','153415]']
            #memPos[1][:-2] = '153415]'[:-2] = '153415' --> pass to int
            #value = 11 --> pass to int --> pass to binary
            memPos,value = l.split('=')
            memPos = int(memPos.split('[')[1][:-2])
            value = int(value.strip())
            
            #(value & 2**i) gets the bit i starting from the left of "value" and gives the new
            # value as all 0s except the bit 2^i, which will correspond to bit i of "value".
            # Then returns this new value (...000(value bit i)000...) as an int.
            # This is:
            #  - 11010 & (2**3) = 11010 & 8 = 11010 & 01000 = 01000 = 8
            #  - 11010 & (2**2) = 11010 & 4 = 11010 & 00100 = 00000 = 0
            #  - 11010 & (2**1) = 11010 & 2 = 11010 & 00010 = 00010 = 2
            newMemValue = 0
            for i,bit in enumerate(reversed(mask)):
                if bit == 'X':
                    newMemValue += (value & 2**i)
                elif bit == '1':
                    newMemValue += (2**i)
                elif bit == '0':
                    pass

            memory[memPos] = newMemValue
    return memory

#1rst part "main"
def p14(fileName, part):
    with open(fileName, 'r') as f:
        lines = [l.strip() for l in f]
        memory = {}
        if part == 1:
            memory = decoderV1(lines)
        elif part == 2:
            memory = decoderV2(lines)

        #Get the sum of memory positions values
        result = 0
        for pos in memory:
            result += memory[pos]
        return result





#Problem 14 solution (part 2) 

#Returns the possibilities of a given address. Looks for an 'X' and
# replaces it with '0' and '1' creating 2 possibilities.
#Then, repeats the process recursively with this 2 new possibilities
# until the address created has not any 'X'. 
def getPossibilities(address,possibilities):
    index = address.find('X')
    if index != -1:
        pos1 = address[:index] + '0' + address[index+1:]
        pos2 = address[:index] + '1' + address[index+1:]
        getPossibilities(pos1,possibilities)
        getPossibilities(pos2,possibilities)

    else:
        possibilities.append(address)

#Decoder for part 2
def decoderV2(lines):
    mask = None   
    memory = {}
    for l in lines:
        if(l.startswith("mask")):
            mask = l.split('=')[1].strip() 
        
        else:
            memPos,value = l.split('=')
            memPos = int(memPos.split('[')[1][:-2])
            value = int(value.strip())
            
            #Creates a modified copy of the address (newAddress) bit by bit. 
            #-If there is an 'X' in the next bit of the mask, it means there is a floating
            #  value so it will keep it in the newAddess as an 'X' so he can get his 
            #  possibilities after getting this copy.
            #-If the bit is '0' or '1' in the next bit of the mask, it ORs it this the corresponding
            #  bit in the address and adds it to the newAddress
            #
            # Example:  address = 1010  and mask = 0X01X0
            #    address -->  001010 }
            #    mask    -->  0X01X0 }
            #  newAddress ->  0X11X0 } = address | mask (except for Xs that are coppied)
            newAddress = ''
            for i,bit in enumerate(reversed(mask)):
                if bit == 'X':
                   newAddress = 'X' + newAddress

                elif bit == '1' or bit == '0':
                    newValue = memPos & 2**i
                    if newValue > 0:
                        newValue = 1

                    newAddress = str(int(bit) | newValue) + newAddress

            #Now with the newAddress, gets the different possible addresses replacing
            # floating values and memory values in that possible addreses are overwritten
            possibilities = []
            getPossibilities(newAddress, possibilities)
            for p in possibilities:
                memory[int(p,2)] = value

    return memory

#2nd part "main"
def p14_2(fileName,part):
    return p14(fileName, 2)


#Main
result = p14('input.txt',1)   
print("P14 ->", result)

result = p14_2('input.txt',2)   
print("P14 ->", result)