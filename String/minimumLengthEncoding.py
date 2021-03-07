"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

- words.length == indices.length
- The reference string s ends with the '#' character.
- For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
"""


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # eliminate duplicate words to store only distinct words
        _set = set(words)
        
        # iterate words in the list
        for word in words:
            # starting from index 1 to end of word, remove all the words in the set that matches
            # the suffix of the current word
            for k in range(1, len(word)):
                _set.discard(word[k:])
                
        # for the remain words in the set, add 1 to the current length of the word, representing #
        return sum(len(word) + 1 for word in _set)
        
# Time complexity: O(n * m), n is the size of the words array and m is the length of the word in the iteration
# Space complexity: O(n), n is the size of the words array