"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        max_val = 0
        stack = [-1]
        
        # Saving the last invalid paranthesis index in stack
        # When a ( comes, store index in stack
        # When a ) come, pop from stack, then check if stack if empty
        # If stack is empty, push index in stack because that's invalid
        # If stack is not empty, check i - top of stack, this will be length of valid substring because top of stack will be index of last invalid paranthesis
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_val = max(max_val, i-stack[-1])
        return max_val