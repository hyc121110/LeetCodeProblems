"""
Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

Example1:
Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.

Example2:
Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
Output: 4
Explanation: [2], [9, 4], [12, 10], [13, 7, 6, 5]
"""

from typing import List

def DecreasingSubsequences(A:List[int])->int:
    """Return a tuple: (min length, list of corresponding subsequences)"""

    from bisect import bisect

    # at last, sequences = [seq0, seq1, seq2, seq3, ...]
    # sequences is not necessary if you only want to find the min length
    sequences = []  
    
    # tails records the last elment of each subseqence. 
    # It is always sorted.
    # tails = [seq0[-1], seq1[-1], seq2[-1], ....]
    tails = []  
    
    for n in A:
        # use a binary search (O(logN)) to greedily find a position
        # we can do this because tails is always sorted
        pos = bisect(tails, n) # this function returns the position of n if n is inserted into tails, which is sorted because of bisect

        if pos == len(tails): # n is the largest number, append a new number to tails
            tails.append(n)
            sequences.append([])
        else:
            sequences[pos].append(tails[pos])
            tails[pos] = n # update the last element of each subsequence
    
    # you don't need the following if you only care about length. Just return len(tails)

    # append each tail to each sequence
    for i, tail in enumerate(tails):
        sequences[i].append(tail)
    
    return len(tails), sequences  