class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            # Base case for succeed
            if total == target:
                #We need to be able to reuse 'curr'
                res.append(curr.copy())
                return

            #Base case for out-of-bound
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i]) 
            #First decision for adding the candidate to total               
            dfs(i, curr, total + candidates[i])
            curr.pop()
            #Secdond decision for moving to next candidate
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res