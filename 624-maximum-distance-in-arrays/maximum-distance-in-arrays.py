class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            n = len(arrays[i])
            res = max(res, max(abs(arrays[i][n - 1] - cur_min), abs(cur_max - arrays[i][0])))

            cur_min = min(cur_min, arrays[i][0])
            cur_max = max(cur_max, arrays[i][n - 1])
        
        return res