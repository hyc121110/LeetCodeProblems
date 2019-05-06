def searchRange(nums, target):
    # create two binary search trees
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            # >= because account for last index equal to itself
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    if target not in nums:
      # instant return if not found    
        return [-1, -1]
    # else start finding the next number after target (smart way)
    lo = search(target)
    return [lo, search(target+1)-1]

nums = [10,11,11,13,14]
target = 11
result = searchRange(nums, target)
print(result)