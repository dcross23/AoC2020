def parseInput(lines):
    foods = []
    for l in lines:
        l = l.replace('contains ','').replace(')','')
        ingredients = [i.strip() for i in l[:l.index('(')-1].strip().split()]
        allergens = [a.strip() for a in l[l.index('(')+1:].strip().split(',')]
        foods.append([ingredients, allergens])
    return foods

#Return True if there are no more allergens to process in any of the foods
def areMoreAllergens(foods):
    for f in foods:
        if len(f[1]) > 0:
            return False
    return True

#Problem 21 solution (part 1) 
def p21(fileName, part):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]  
        foods = parseInput(lines)

        if part == 2:
            CDIList = {}

        while not areMoreAllergens(foods):
            #Get the next food with allergens to process
            for f in foods:
                if len(f[1]) > 0:
                    food = f

            for allergen in food[1]:
                #Get the foods that contain that allergen
                foodsWithAllergen = []
                for f in foods:
                    if food!=f and allergen in f[1]:
                        foodsWithAllergen.append(f)



                #Look for an ingredient that is common in foods with that allergen
                commonIng = None
                for ing in food[0]:
                    inAll = True
                    for fwa in foodsWithAllergen:
                        if ing not in fwa[0]:
                            inAll = False
                            break
                    if inAll:
                        commonIng = ing
                        break

                if part == 2:
                    CDIList[allergen] = commonIng 

                #Now we have a common ingredient associated with a allergen, so we can
                # remove them from all the lists
                for f in foods:
                    if commonIng in f[0]:
                        f[0].remove(commonIng)
                    if allergen in f[1]:
                        f[1].remove(allergen)
 
        if part == 1:
            return [sum(len(f[0]) for f in foods)][0]
        
        elif part == 2:
            s = ''
            for k in sorted(CDIList):
                if s == '': s = CDIList[k]
                else: s += ',' + CDIList[k]

            return s


#Problem 21 solution (part 2) 
def p21_2(fileName, part):
    return p21(fileName, part)


#Main
result = p21('input.txt',1)   
print("P21 ->", result)

result = p21_2('input.txt',2)   
print("P21_2 ->", result)