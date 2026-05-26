class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # seen = set()

        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen.add(i)
        # return i

        nums.sort()
        return nums[len(nums) // 2]