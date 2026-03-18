n = 2


class Solution:
    """
    Main idea would be like find iteration as n - 2 and after iteration + last summary of variants past iteration,
    but I really don`t know how realize this version in code. But Gemini helps me and give idea about Fibonacci numbers
    and his formula to solve this exercise.
    """
    def climb_stairs(self, n: int) -> int: # Use Fibonacci formula for solve this exercise
        t = n - 2
        if n == 1:
            summary_of_variants = n
            return summary_of_variants
        if 2 <= n <= 45:
            summary_of_variants = (t**2 + t + 4) / 2
            return int(summary_of_variants)


solution = Solution()
print(solution.climb_stairs(n))