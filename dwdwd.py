str1 = "ABCABC"
str2 = "ABC"


class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        liststr1 = [letter for letter in str1]
        liststr2 = [letter for letter in str2]
        liststr3 = liststr1.count(liststr2)
        print(liststr3)
        print(liststr1, liststr2)


solution = Solution()
print(solution.gcd_of_strings(str1, str2))