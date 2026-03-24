nums = [2,14,18,22,22]


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        if 1 <= len(nums) <= 10**5:
            for element in range(0, len(nums)):
                if -10**9 <= nums[element] <= 10**9:
                    for element2 in range(element + 1, len(nums)):
                        if nums[element] == nums[element2]:
                            return True
            return False


solution = Solution()
print(solution.contains_duplicate(nums))