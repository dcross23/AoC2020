#Uses the expression as a stack, so it calculates simple expresions like
# num1 (+ or *) num2, removing this 3 elements from the expression and adding
# the result of it.
#For example -> 1+2*3+4*5
# The algorithm will do:
# 1+2*3+4*5 -> 1+2*3+20 -> 1+2*23 -> 1+46 -> 47  (returns 47)
#
#IMPORTANT: The expression has to be passed reversed
def evaluateSimpleExpresionNoPrecedences(expression):
    while len(expression) > 1:
        num1 = expression.pop()
        operator = expression.pop()
        num2 = expression.pop()

        if operator == '+':
            expResult = num1 + num2
        elif operator == '*':
            expResult = num1 * num2

        expression.append(expResult)

    return expression[0]
            

#Now, operator + has more precedence than operator *
#
#First, it calculates all simple expresions that are like
# num1+num2. If the operator finded is *, just copies num1 
# to the stack, leaving num2 in case is part of a sum.
#For example -> 1+2*3+4*5 -> will leave the stack as -> 
#            -> 5*7*3 -> stack=[5,7,3] 
# It is reversed because we add to the stack at the end. It doesnt 
#  matter because multiplication is conmutative.
#
#Then, the algorith just calculates this multiplications storing the
# result in an acumulator:
#With the example above -> 5*7*3:
#   acum=1 -> acum=1*5=5 -> acum=5*7=35 -> acum=35*3=105
#Then, it just returns the accumulator (solution to the expression)
def evaluateSimpleExpresionWithPrecedences(expression):
    stack = []
    while len(expression) > 1:
        num1 = expression.pop()
        operator = expression.pop()

        if operator == '+':
            num2 = expression.pop()
            expResult = num1 + num2
            expression.append(expResult)

        elif operator == '*':
            stack.append(num1)

    stack.append(expression[0])
    acum = 1
    while len(stack) > 1:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1*num2)

    return stack[0]
            

#It just leave the expression at it is, replacing expressions inside
# parenthesis to the result of it, and saving it in the stack. This is:
#For example: 1+(2*3)+4 -> stack=1+6+4
#
#Then, it just calls the specific method above to evaluate the expression
# (depending if there is precedence or not) with the stack that is the 
# simplified version (no parenthesis) of the original expression and
# returns the result.
def solveParenthesisExpresions(expression, part):
    stack = []
    for element in expression:
        if element != ')':
            stack.append(element)
        
        else:
            newExpresion = []
            while stack[-1] != '(':
                newExpresion.append(stack.pop())

            stack.pop()
            if part == 1:
                stack.append(evaluateSimpleExpresionNoPrecedences(newExpresion))
            else:
                stack.append(evaluateSimpleExpresionWithPrecedences(newExpresion))

    if part == 1:
        return evaluateSimpleExpresionNoPrecedences(list(reversed(stack)))
    else:
        return evaluateSimpleExpresionWithPrecedences(list(reversed(stack)))


#Problem 18 solution (part 1) 
def p18(fileName, part):
    with open(fileName, 'r') as f:
        lines = [line.strip() for line in f]  
        
        total = 0
        for i,expression in enumerate(lines):
            lines[i] = lines[i].replace('(', '( ').replace(')', ' )').split(' ')
            lines[i] = [int(x) if x not in ['+','*','(',')'] else x for x in lines[i]]
            total += solveParenthesisExpresions(lines[i], part)

        return total

#Problem 18 solution (part 2) 
def p18_2(fileName, part):
    return p18(fileName, part)

#Main
result = p18('input.txt',1)   
print("P18 ->", result)

result = p18_2('input.txt',2)   
print("P18_2 ->", result)