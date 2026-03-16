nums = [2,2]
target = 4


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if 2 <= len(nums) <= 10 ** 4 and -10 ** 9 <= nums[i] <= 10 ** 9 and -10 ** 9 <= target <= 10 ** 9:
                    if nums[i] + nums[j] == target:
                        return [i, j]


solution = Solution()
print(solution.two_sum(nums, target))