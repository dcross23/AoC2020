import re

#Problem 3 solution (part 1)
#Checks if a passport is valid or not
def isValid(passport):
    passPortNeededFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for f in passPortNeededFields:
        if f not in passport:
            return False
    return True

#Loads passports correctly
def loadPassports(fileName):
    with open(fileName, 'r') as f:
        lines = [ line.strip() for line in f]

        passPorts = []
        passport = ''
        for i,line in enumerate(lines):            
            #if the line is not empty
            if line != '':
                passport += line + ' '
                
                if i == len(lines)-1:
                    passPorts.append(passport.strip())
            else:
                passPorts.append(passport.strip())
                passport = ''
                
        return passPorts
    return []
    
#1rst part
def p4(fileName):
    validPassPorts = [p for p in loadPassports(fileName) if isValid(p)]
    return len(validPassPorts), validPassPorts

#Problem 3 solution (part 2)
def isNowValid(passPort):
    for field in passPort.split(' '):
        name = field.split(':')[0]
        value = field.split(':')[1]
        
        if name == 'byr' and (int(value)<1920 or int(value)>2002):
            return False
            
        if name == 'iyr' and (int(value)<2010 or int(value)>2020):
            return False  
            
        if name == 'eyr' and (int(value)<2020 or int(value)>2030):
            return False    
            
        if name == 'hgt':
            if value.endswith('cm'):
                if (int(value[:-2])<150 or int(value[:-2])>193):
                    return False
                    
            elif value.endswith('in'):
                if (int(value[:-2])<59 or int(value[:-2])>76):
                    return False
            else:
                return False
            
        if name == 'hcl' and not re.search("#[0-9a-fA-F]{6}", value):
            return False
            
        if name == 'ecl' and value not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False
            
        if name == 'pid' and len(value) != 9:
            return False
            
    return True

def p4_2(fileName, validPassPorts):
    newValidPassPorts = [p for p in validPassPorts if isNowValid(p)]
    return len(newValidPassPorts), newValidPassPorts        
       

#Main
file = 'input.txt'
result, validPassPorts = p4(file)
print("P4 ->",result)

result, newValidPassPorts = p4_2(file, validPassPorts)
print("P4_2 ->",result)