'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
'''

def generateParenthesis(n):
    parens=[]
    def generate(p, left, right):
        # possible to open paren -> reduce left by 1
        if left:
            generate(p + '(', left-1, right)
        # possible to close paren -> reduce right by 1
        if right > left:
            generate(p + ')', left, right-1)
        # no more paren to close -> end of string (backtracking)
        if not right:
            parens.append(p)
        return parens
    return generate('', n, n)

n = 3
result = generateParenthesis(n)
print(result)