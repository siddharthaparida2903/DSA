class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for c1, c2 in zip(s, t):
            if c1 != c2:
                return c2
        return t[-1]