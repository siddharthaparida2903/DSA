class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        nums = [num for row in mat for num in row]

        return [nums[i:i + c] for i in range(0, len(nums), c)]