'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.
'''

'''
Sort the words by word's length. (also can appply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.
'''

def longestStrChain(words):
  dp = {}
  
  # sort the words based on length
  for w in sorted(words, key=len):
    # '+' concatenate strings
    dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))

  return max(dp.values())

print(longestStrChain(words=["a","b","ba","bca","bda","bdca"]))