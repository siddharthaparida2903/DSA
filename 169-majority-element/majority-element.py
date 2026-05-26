class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ## BOYER-MOORE METHOD (O(1))
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

        ## HASH MAP METHOD (O(n))
        # count = {}
        # res = maxCount = 0

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        #     res = num if count[num] > maxCount else res
        #     maxCount = max(count[num], maxCount)
        # return res

        ## SORTING METHOD
        # nums.sort()
        # return nums[len(nums) // 2]

