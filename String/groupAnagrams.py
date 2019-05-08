'''
Given an array of strings, group anagrams together.
'''

def groupAnagrams(strs):
  d = {}

  for w in strs:
    # key is a tuple with characters sorted alphabetically
    key = tuple(sorted(w))
    # value of the key is either key (which is a tuple) or an empty list
    # 1. if key doesn't exist, add the word to a empty list
    # 2. if key exists, simply extend the existing list
    d[key] = d.get(key, []) + [w]
  # values of the dict are lists of strings
  return list(d.values())

print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))