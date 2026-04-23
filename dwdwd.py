nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        current_sum = max_total = nums[0]

        for x in nums[1:]:
            current_sum = max(x, current_sum + x)
            max_total = max(max_total, current_sum)

        return max_total


solution = Solution()
print(solution.max_sub_array(nums))