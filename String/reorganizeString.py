'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
'''

def reorganizeString(S):
    # sort array based on occurence of characters
    a = sorted(sorted(S), key=S.count)
    # obtain median of the array
    h = len(a) // 2
    # odd indices: character with less occurence
    # even indices: character with more occurence
    a[1::2], a[::2] = a[:h], a[h:]
    # if the last two characters are the same, return nothing because
    # there are at least two same adjacent characters
    # else return new string ('*' ensure return nothing or reorganized string)
    return ''.join(a) * (a[-1:] != a[-2:-1])

print(reorganizeString(S="abaabbaabb"))