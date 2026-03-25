#store every opening into a stack
#for every closing part of the pair
#check if its counterpart that is stored within a hash is on top
#of the stack, and pop that and if it is, for all. Return True
class Solution:
    def isValid(self, s: str) -> bool:
        openingStack = []
        pairsD = {']':'[', '}':'{', ')':'('}

    #needs to check if its openinig bracket then just append
    #if its closing bracket then we want to check for its opening bracket

        for char in s:
            if char in list(pairsD.values()):
                openingStack.append(char)
                continue
            if char in pairsD.keys():
                if len(openingStack) < 1:
                    return False
                elif openingStack.pop() != pairsD[char]:
                    return False
            
        if len(openingStack) < 1:
            return True
        return False