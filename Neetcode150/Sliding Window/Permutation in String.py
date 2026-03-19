#my logic is:
#get first 0 - len(s1) substr as a freq count in a premade 26* char array
#use sliding window to remove the l and add the r char for each window iteration
#return True when the frequency of both arrays match

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 

        s1array = [0]*26
        s2array = [0]*26
        
        #fills up the s1array
        while l < len(s1): 
            s1array[ord(s1[l])-ord('a')] += 1
            l += 1

        l = 0
        for r in range(len(s2)):
            #if the the window is bigger then the len the substr will never match
            #move left pointer
            while r - l + 1 > len(s1):
                s2array[ord(s2[l])-ord('a')] -= 1
                l += 1

            #this adds the char at pointer r to s2array
            s2array[ord(s2[r])-ord('a')] += 1
            if s1array == s2array:
                return True
        return False
            
            
            



        