class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        res = []

        for i in range(len(s) - 1, -1, -k):
            start = max(0, i - k + 1)
            res.append(s[start:i + 1])

        return "-".join(res[::-1])