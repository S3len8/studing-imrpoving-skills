n = 5


class Solution:
    """
    Main idea would be like find iteration as n - 2 and after iteration + last summary of variants past iteration,
    but I really don`t know how realize this version in code. But Gemini helps me and give idea about Fibonacci numbers
    and his formula to solve this exercise.
    """
    def climb_stairs(self, n: int) -> int: # Use Fibonacci formula for solve this exercise
        for i in range(n):
            for j in range(i+1, n):
                if n == 1 or n == 2:
                    return n
                if n > 2:
                    t = 2
                    summary = t + j
                    print(t, j, i)
                    print(summary)



solution = Solution()
print(solution.climb_stairs(n))