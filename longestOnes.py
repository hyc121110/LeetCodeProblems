def longestOnes(A, K):
    i = 0
    for j in range(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1

print(longestOnes(A=[1,1,1,0,0,0,1,1,1,1,0], K=2))