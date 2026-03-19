#main things to know:
#the window is only valid if len of window - biggest freq of char < k
#if not move left up
#for loop naturally moves the window if valid still
#returns the greatest len with r - l + 1 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        #implement a sliding window
        l = 0
        #r pointer naturally gets incremented
        for r in range(len(s)):
            #this populates the dict w counter for each char(max:26)
            count[s[r]] = count.get(s[r], 0) + 1 
            #this checks if the len(r-l+1) - the greatest count is greater 
            #then k, which means it is invalid to keep going for the window
            while r - l + 1 - max(count.values()) > k:
                #we just move the l pointer and decrease the count of l by 1
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


             