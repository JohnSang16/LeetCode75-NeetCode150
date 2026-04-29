# basic implementation of binary search
# l, r, mid tracker. l is 0, r is length - 1, and mid is l + r // 2 
# we check if target in a sorted arr is equal to mid if not we move l or r pointer up or down
# keep repeating until we find 
# if we don't find it we return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2 

            if target > nums[mid]:
                l = mid + 1 
            elif target  < nums[mid]:
                r = mid - 1 
            else:
                return mid

        return -1