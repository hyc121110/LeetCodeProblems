"""
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
"""

def wiggleMaxLength(nums):
    # 2 pointers to store the max and min peaks
    # we update up when the prev difference was negative
    # alternatively, we update down when the prev difference was positive
    # if the next number has the same positve/negative gain
    # the pointer will remain the same
    up = 1
    down = 1
    for i in range(1,len(nums)):
        if (nums[i] > nums[i-1]):
            up = 1 + down
        elif (nums[i] < nums[i-1]):
            down = 1 + up
    
    
    return max(up, down)

print(wiggleMaxLength([1,7,4,9,2,5]))