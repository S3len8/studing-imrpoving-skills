# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5,1001]
nums2 = [9,4,9,8,4,1001]


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result_nums1 = []
        result_nums2 = []

        if 1 <= len(nums1) <= 1000 and 1 <= len(nums2) <= 1000:
            for i in range(0, len(nums1)):
                if 0 <= nums1[i] <= 1000:
                    n = nums1[i]
                    result_nums1.append(n)
            for i in range(0, len(nums2)):
                if 0 <= nums2[i] <= 1000:
                    u = nums2[i]
                    result_nums2.append(u)

        nums1set = set(result_nums1)
        nums2set = set(result_nums2)

        return list(nums1set.intersection(nums2set))


solution = Solution()
print(solution.intersection(nums1, nums2))

