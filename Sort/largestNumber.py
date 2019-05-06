import functools

def largestNumber(nums):
    # function to compare numbers
    compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
    # convert int to string
    _nums = list(map(str, nums))
    # sort array based on function
    _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
    # concatenate strings
    return str(int(''.join(_nums)))
    
print(largestNumber(nums=[3,30,34,5,9]))