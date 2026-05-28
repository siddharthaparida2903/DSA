class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t, b = 0, len(matrix)
        l, r = 0, len(matrix[0])

        # base case
        while t < b and l < r:
            # all element in the top
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            # all elements in the right
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not(t < b and l < r):
               break

            # all elements in the bottom
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            #all elements in the left
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        return res 