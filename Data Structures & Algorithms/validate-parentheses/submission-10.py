class Solution:
    def isValid(self, s: str) -> bool:
        closedtoopen = {"]":"[", "}":"{",")":"("}
        stack=[]

        for c in s:
            if c in closedtoopen:
                if stack and stack[-1]== closedtoopen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        return True if not stack else False
            