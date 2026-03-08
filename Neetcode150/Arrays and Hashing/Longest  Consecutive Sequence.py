#first check if the num is the starting val of a seq
#if so check how long the seq is and store it 
#return the longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1 
                longest = max(length, longest)
        return longest
                