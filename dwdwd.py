nums = [3,0,1]


class Solution:
    def missing_number(self, nums: list[int]) -> int:
        solve_all_numbers = (len(nums) * (len(nums) + 1)) / 2
        solve_nums_numbers = sum(nums)
        return int(solve_all_numbers - solve_nums_numbers)


solution = Solution()
print(solution.missing_number(nums))