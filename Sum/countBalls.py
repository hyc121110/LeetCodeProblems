"""
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
"""

"""
Using a dictionary and a counter to track the largest value
"""
def countBalls(self, lowLimit: int, highLimit: int) -> int:
    
    d = {}
    largest_value = 0
    for num in range(lowLimit, highLimit+1):
        s = 0
        while num > 0:
            reminder = num % 10
            s += reminder
            num = num // 10
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
        if d[s] > largest_value:
            largest_value = d[s]
    
    return largest_value