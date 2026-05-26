class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i, n in enumerate(nums):
            content = target - n

            if content in prevMap:
                return [prevMap[content], i]
            
            prevMap[n] = i

        return
