'''
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
'''

def equationsPossible(equations):
    UF = {}
        
    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]
    
    for equation in equations:
        x, e1, _, y = equation
        if x not in UF:
            UF[x] = x
        if y not in UF:
            UF[y] = y
        if e1 != '!':
            UF[find(x)] = find(y)
    
    for equation in equations:
        x, e1, _, y = equation
        if e1 == '=' and find(x) != find(y): return False
        if e1 == '!' and find(x) == find(y): return False
    
    return True

print(equationsPossible(equations=["a==b","b!=c","c==a"]))
print(equationsPossible(equations=["a==b","b==c","a==c"]))
print(equationsPossible(equations=["c==c","b==d","x!=z"]))
print(equationsPossible(equations=["a!=a"]))
