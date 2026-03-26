nums = [0,1,0,3,12]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Возврат значения не требуется, все изменения выполняются на месте.
        """
        if 1 <= len(nums) <= 10**4:
            for num in nums:
                if num == 0 and -2**31 <= nums[num] <= 2**31 - 1:
                    nums.remove(0)
                    nums.append(0)

        print(nums)


solution = Solution()
print(solution.moveZeroes(nums))

# count_nums = nums.count(0)
# i = 0
# while i < count_nums:
#     print(i)
#     nums.pop(0)
#     nums.append(0)
#     i += 1