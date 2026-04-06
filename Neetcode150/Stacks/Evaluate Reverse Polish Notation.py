#make a postfix operator work with stacks
#1st step keep pushing to stack if not an operator
#2nd step pop from stack when operator is hit and use that operator on the items
#3rd step whatever it returns gets pushed to the stack

import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        dictOperators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : lambda a,b: int(a/b)}
        for i in range(len(tokens)):
            if tokens[i] == '':
                continue
            #step 1 
            if tokens[i] not in dictOperators:
                stack.append(int(tokens[i]))
            #step 2
            else:
                b = stack.pop()
                a = stack.pop()
                operation = dictOperators[tokens[i]](a,b)
            #step 3 
                stack.append(operation)
        return stack.pop()