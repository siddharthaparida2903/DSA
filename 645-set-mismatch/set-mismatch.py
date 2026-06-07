class Solution:
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = (n * (n + 1)) // 2 - (sum(seen))

        return [duplicate, missing]