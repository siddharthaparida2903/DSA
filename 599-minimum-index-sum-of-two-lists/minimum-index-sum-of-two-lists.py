class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {name: i for i, name in enumerate(list1)}

        min_sum = float('inf')
        res = []

        for j, name in enumerate(list2):
            if name in pos:
                idx_sum = pos[name] + j

                if idx_sum < min_sum:
                    min_sum = idx_sum
                    res = [name]
                elif idx_sum == min_sum:
                    res.append(name)

        return res