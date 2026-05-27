class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ## 2-POINTER METHOD
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

        ## SORTING METHOD
        # unique = sorted(set(nums))
        # nums[:len(unique)] = unique
        # return len(unique)