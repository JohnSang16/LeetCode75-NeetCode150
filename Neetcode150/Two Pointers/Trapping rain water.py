#area is h * w 
#check if there is boundaries for each space to hold water 
#by using l pointer @ 0 and another at that is the val at 
#pointer 1 or greater, then calculate that area
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = 1
        area = 0
        while l <= r:
            if height[l] > 0 and height[r] < height[l]: 
                pass
    