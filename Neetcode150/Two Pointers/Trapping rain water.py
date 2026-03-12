#the Solution is to use two pointers
#left pointer iterates if height[l] less then right pointer at height[r]
#this is because we just need the minimum value of the two
#then we calculate whichever side is the minimum - height[minpointer]
#then update the new max value if found, and then add to res
#return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
  
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
