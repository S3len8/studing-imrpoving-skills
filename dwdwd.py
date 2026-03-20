s = "abccccdd"


class Solution:
    def longest_palindrome(self, s: str) -> int:
        single_letter = False
        result = []
        count_letters_list = []
        for element in s:
            result.append(element)
        for k in range(len(result)):
            count_letters = result.count(result[k])
            # print(count_letters)
            if count_letters == 1:
                if not single_letter:
                    count_letters_list.append(result[k])
                    single_letter = True
            else:
                count_letters_list.append(result[k])
            # for v in range(k + 1, len(result)):
                # print(result.count(result[k]))
                # print(f"Haven`t any similar letter")


        print(result)
        print(count_letters_list)


solution = Solution()
print(solution.longest_palindrome(s))