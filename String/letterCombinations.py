'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

def letterCombinations(digits):
    map_ = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz'
    }
    result = []

    # helper function
    def make_combinations(i, cur):
        # at the end of the list -> concatenate chars in cur and add to result
        if len(digits) == 0:
            return
        if i == len(digits):
            result.append(''.join(cur))
            return
        for ch in map_[digits[i]]:
            cur.append(ch)
            make_combinations(i+1, cur)
            cur.pop()

    make_combinations(0, [])
    return result

print(letterCombinations(digits="23"))