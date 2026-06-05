from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        freq = Counter(nums1)
        result = []

        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result