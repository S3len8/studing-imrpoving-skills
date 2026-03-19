import re

s = "A man, a plan, a canal: Panama"


class Solution:
    def is_palindrome(self, s: str) -> bool:
        if 1 <= len(s) <= 2*10**5:
            clear_str = re.sub(r'[^a-zA-Z0-9\s]', '', s).lower().replace(" ", "")
            if clear_str == "".join(reversed(clear_str)):
                return True
            return False
        return True


solution = Solution()
print(solution.is_palindrome(s))