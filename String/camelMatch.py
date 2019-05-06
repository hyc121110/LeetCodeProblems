'''
A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.
'''

def camelMatch(queries, pattern):
    def pat_match(str, pat):
        # init pointer
        ptr = 0
        for s in str:
            if ptr < len(pat) and s == pat[ptr]:
                # if char matches pattern char, move pointer to check the next one
                ptr += 1
            # check if the next symbol is a cap letter as it represents
            # start of a word. If it's not a cap letter, continue
            elif ord('Z') >= ord(s) >= ord('A'):
                # if not match and it's a cap letter
                return False
        # if j != len(pat), there are mismatching lower case letters 
        return ptr == len(pat) 
    if not queries:
        return False
    res = []
    # ascii for cap letters: from 65 to 90
    for query in queries:
        res.append(pat_match(query,pattern))

    return res

queries=["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
print(camelMatch(queries,pattern))