"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""

# solution:
# since the sum of operation from left to right and right to left is length of the string,
# we can use len(s)-c1 to get the number of operation from the other side

# the solution must be 010101... or 101010... so we can use i % 2 to check if it is matching,
# if not match, we increment 1
# last, check the opposite side by using len(s)-c1
def minOperations(self, s: str) -> int:
    c1 = 0
    for i, n in enumerate(s):
        if i % 2 != int(n):
            c1 += 1
    return min(c1, len(s)-c1)