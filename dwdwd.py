s = "prog*ram**mer"


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if 1 <= len(s) <= 10**5:
                if char == '*':
                    # Если встретили звезду, удаляем последнюю добавленную букву
                    if stack:
                        stack.pop()
                else:
                    # Если это буква, кладем её в стек
                    stack.append(char)

        # Собираем список обратно в строку
        return "".join(stack)


solution = Solution()
print(solution.removeStars(s))