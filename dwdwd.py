height = [1,2,4,3]


class Solution:
    def max_area(self, height: list[int]) -> int:
        result = []
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if 2 <= len(height) <= 10**5 and 0 <= height[i] <= 10**4:
                    length = j - i
                    if height[i] >= height[j]:
                        area = height[j] * length
                        result.append(area)
                    if height[j] >= height[i]:
                        area = height[i] * length
                        result.append(area)
                    if len(height) <= 2:
                        area = min(height) * 1
                        result.append(area)
        return max(result, default=0)


solution = Solution()
print(solution.max_area(height))