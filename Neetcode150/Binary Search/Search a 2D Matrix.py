class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1    
        n = len(matrix[0])
        while l <= r:
            mid = (l + r)//2
        
            if target < matrix[mid // n][mid % n]:
                r = mid - 1
            elif target > matrix[mid // n][mid % n]:
                l = mid + 1
            else:
                return True
        return False

