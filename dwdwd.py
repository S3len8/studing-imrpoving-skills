import math
piles = [3, 6, 7, 11]
h = 8


class Solution:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        sum_banana = 0
        for banana in piles:
            sum_banana += banana

        if len(piles) < h:
            nim_time_eating = sum_banana / h
            return math.ceil(nim_time_eating)

        if len(piles) == h:
            nim_time_eating = max(piles)
            return math.ceil(nim_time_eating)

        # if len(piles) < h:
        #     half_max_one = max(piles) / 2
        #     hals_max_two = max(piles) / 2
        #     for i in range(len(piles)):
        #         if  piles[i] == max(piles):
        #             piles[i] = half_max_one
        #             piles.append(hals_max_two)
        #
        #     nim_time_eating = max(piles)
        #     return math.ceil(nim_time_eating)


solution = Solution()
print(solution.min_eating_speed(piles, h))