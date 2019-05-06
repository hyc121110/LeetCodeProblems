'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.
'''

def uniqueDigits(n):
    if n == 0: return 1
    # base case with n = 1
    res = 10
    remainDigits = 9
    uniqueDigits = 9
    n -= 1
    while n and remainDigits:
        uniqueDigits *= remainDigits
        res += uniqueDigits
        remainDigits -= 1
        n -= 1
    return res
        
print(uniqueDigits(n=2))