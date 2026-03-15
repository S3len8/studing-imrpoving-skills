nums = [-1,0,3,5,9,12]
target = 9


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if 1 <= len(nums) <= 10**4:
            for i in nums:
                if (-10**4 >= i or i >= 10**4) or (-10**4 >= target or target >= 10**4):
                    return -1
                if i == target:
                    return nums.index(i)
                if target not in nums:
                    return -1


solution = Solution()
print(solution.search(nums, target))

