class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        ## SORTING METHOD
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)