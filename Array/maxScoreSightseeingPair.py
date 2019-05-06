'''
Given an array A of positive integers, A[i] represents the value of the i-th 
sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : 
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
'''

'''
Intuition:
Count the current best score in all previous sightseeing spot.
Note that, as we go further, the score of previous spot decrement.

Explanation
cur will record the best score that we have met.
We iterate each value a in the array A,
update res by max(res, cur + a)

Also we can update cur by max(cur, a).
Note that when we move forward,
all sightseeing spot we have seen will be 1 distance further.

So for the next sightseeing spot cur = Math.max(cur, a) **- 1**

It's kinds of like, "A near neighbor is better than a distant cousin."

Time Complexity:
One pass, O(N) time, O(1) space
'''
def maxScoreSightseeingPair(A):   
    # cur: current value given current index
    # res: value to return
    cur = res = 0
    for a in A:
        res = max(res, cur + a)
        cur = max(cur, a) - 1 # A[i] + i - distance between cur and next ptr
    return res
    
print(maxScoreSightseeingPair([8,1,5,2,6]))

