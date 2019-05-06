'''
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
'''

def shipWithinDays(weights, D):
    # 1st solution:
    # set left and right for min and max weight needed
#    l,r = max(weights), sum(weights)
#    
#    while l < r:
#        mid, need, cur_weight = (l + r) // 2, 1, 0
#        for w in weights:
#            # binary search to find the required weight
#            # is less than or more than the mid value
#            if cur_weight + w > mid:
#                # exceeded, increment bags needed, reset cur_weight
#                need += 1
#                cur_weight = 0
#            if need > D: break
#            # add w to cur_weight for next weight
#            cur_weight += w
#        if need > D:
#            # days needed exceed required days, move l to the right
#            # to store more weights per day
#            l = mid + 1
#        else:
#            r = mid
#    return l
    
    # 2nd solution: 
    # l and r are more strict
    avg = sum(weights) // D
    left, right = max(avg, max(weights)), 2*avg
    while left < right:
        mid, need, cur = (left + right)>>1, 1, 0
        for w in weights:
            if cur + w > mid:
                need += 1
                cur = 0
            if need>D:break
            cur += w
        if need > D: left = mid + 1
        else: right = mid
    return left

print(shipWithinDays(weights=[1,1,1,24],D=3))