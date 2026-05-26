class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # defined a set to store array values

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False 

