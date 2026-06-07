class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse=True)

        pos = {}
        for i, s in enumerate(ranks):
            if i == 0:
                pos[s] = "Gold Medal"
            elif i == 1:
                pos[s] = "Silver Medal"
            elif i == 2:
                pos[s] = "Bronze Medal"
            else:
                pos[s] = str(i + 1)

        return [pos[s] for s in score]