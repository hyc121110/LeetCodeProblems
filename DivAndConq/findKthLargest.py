'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

def findKthLargest(nums, k):

	# Median-of-Three Partitioning: 
	# Use the median of the three elements on the left, right, 
	# and middle positions as the pivot element.
	# Hide pivot finally
    def Medium3(nums, left, right):
        center = (left + right) // 2
        if nums[left] > nums[center]:
            nums[left], nums[center] = nums[center], nums[left]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[center] > nums[right]:
            nums[center], nums[right] = nums[right], nums[center]
        # Invariant: points[left] <= points[center] <= points[right]
        nums[center], nums[right - 1] = nums[right - 1], nums[center] # Hide pivot in the penultimate position
        return nums[right-1] # Return pivot

    def Qselect(nums, k, left, right):
        if left < right:
            pivot = Medium3(nums, left, right)
            i = left; j = right - 1
            while i < j:
		    # plus 1 first to avoid infinite loop
                i += 1
                while nums[i] < pivot: i += 1
                j -= 1
                while nums[j] > pivot: j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
		# restore pivot
            nums[i], nums[right - 1] = nums[right - 1], nums[i]
            if k <= i:
                Qselect(nums, k, left, i - 1)
            elif k > i + 1:
                Qselect(nums, k, i + 1, right)

    Qselect(nums, len(nums)+1-k, 0, len(nums) - 1)
    return nums[len(nums)-k]