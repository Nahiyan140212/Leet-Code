'''
Key idea of this stack solution is that all opening parentheses will be added to a list and then subsequently removed using list.pop() function if their corresponding closing parentheses are matched.

Matching: Innermost pair has to be a parenthesis containing nothing. That is (), [] or {}. And the opening parenthesis of this pair will be removed first. Once all opening parenthesis are removed, stack == [], which will return True.

Therefore stack.pop() is to remove the last item in stack progressively so as to make it a null list.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"]":"[", "}": "{", ")":"("}
        
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
        return stack == []
            
