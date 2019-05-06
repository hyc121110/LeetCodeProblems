'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
'''

def longestArithSeqLength(A):
    diff = {}
    
    # start from first index
    for i in range(len(A)):
        # start from second index
        for j in range(i+1, len(A)):
            # get the length of the longest artithmetic sequence
            # if doesn't exist, initialize the length to 1 + 1 = 2
            # store (index, difference) as key
            diff[j, A[j] - A[i]] = diff.get((i, A[j] - A[i]), 1) + 1
    return max(diff.values())
print(longestArithSeqLength(A=[20,1,15,3,10,5,8]))