class Solution:
    def isValid(self, s: str) -> bool:
        closedtoOpen = {")": "(", "]": "[", "}": "{"}
        stack=[]

        for c in s:
            if c in closedtoOpen:
                if stack and stack[-1] == closedtoOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        return True if not stack else False




