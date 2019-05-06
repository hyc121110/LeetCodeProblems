'''
Given a collection of intervals, merge all overlapping intervals.
'''

def merge(intervals):
    if not intervals:
        return []
    # sort intervals by start
    intervals.sort(key=lambda x: x.start)
    arr = []
    current = intervals[0]

    for interval in intervals[1:]:
        # end of left arr < start of right arr
        if current.end < interval.start:
            # no conflict, add left arr
            arr.append(current)
            # update left arr for next iteration
            current = interval
        else:
            # update left end comparing the two arr
            current.end = max(current.end, interval.end)
    arr.append(current)
    return arr
    
print(merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))