'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''

def sortColors(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  red, white, blue = 0, 0, len(nums)-1
    
  while white <= blue:
    # move red to the right
    if nums[white] == 0:
      nums[red], nums[white] = nums[white], nums[red]
      white += 1
      red += 1
    # don't need to move
    elif nums[white] == 1:
      white += 1
    else:
      # move blue to the back of the list
      nums[white], nums[blue] = nums[blue], nums[white]
      blue -= 1

sortColors([1,1,2,0,2,1,1,0])