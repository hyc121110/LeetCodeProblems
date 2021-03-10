"""
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.
"""

# time complexity: O(nlogn), n to iterate total_gain and log n to sort the total gain array

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        if sum1 == sum2:
            return 0
        elif sum1 < sum2:
            larger_sum = nums2
            smaller_sum = nums1
        else:
            larger_sum = nums1
            smaller_sum = nums2
        
        target_difference = abs(sum1 - sum2)
        
        # calculate max gain for each position
        # arr with larger sum need to reduce as much as possible
        # arr with smaller sum need to increase as much as possible
        larger_max_gain = [larger_sum[i]-1 for i in range(len(larger_sum))]
        smaller_max_gain = [6-smaller_sum[i] for i in range(len(smaller_sum))]
        
        # join the two gain array and sort the gains by descending order
        total_gain = larger_max_gain + smaller_max_gain
        total_gain.sort(reverse=True)
        
        res = 0
        for i in range(len(total_gain)):
            target_difference -= total_gain[i]
            res += 1
            
            if target_difference <= 0:
                # it is possible
                return res
        
        # reaches here if target_difference is still larger than 0
        return -1