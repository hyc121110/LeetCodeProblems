'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
'''

from collections import defaultdict
import bisect

class TimeMap(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.times = defaultdict(list)
    self.values = defaultdict(list)

  def set(self, key, value, timestamp):
    """
    :type key: str
    :type value: str
    :type timestamp: int
    :rtype: None
    """
    self.times[key].append(timestamp)
    self.values[key].append(value)

  def get(self, key, timestamp):
    """
    :type key: str
    :type timestamp: int
    :rtype: str
    """
    # bisect: This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered
    idx = bisect.bisect(self.times[key], timestamp)
    # return the value in previous item in kv[key]
    return '' if idx == 0 else self.values[key][idx-1]
    