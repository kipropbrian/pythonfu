from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, 1
        
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                print(i, k)
        return [0]          


x = Solution()
x.twoSum([1,2,3,6,88], 8)

