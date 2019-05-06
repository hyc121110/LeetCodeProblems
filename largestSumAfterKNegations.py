# choose largest negative number by sorting

def largestSumAfterKNegations(A, K):
    # method 1: naive solution
    # while K > 0:
    #     min_idx = A.index(min(A))
    #     A[min_idx] = -A[min_idx]
    #     K -= 1
    # return sum(A)
    # method 2: sort first
    A.sort()
    i = 0
    # only convert negative numbers
    while i < len(A) and i < K and A[i] < 0:
        A[i] = -A[i]
        i += 1
    # either add all the numbers in the list when (K - i) % 2 == 0
    # or add all and subtract the smallest positve number times 2
    # (calculate the difference if that number is converted)
    return sum(A) - (K - i) % 2 * min(A) * 2

print(largestSumAfterKNegations(A=[4,2,3], K = 1))
print(largestSumAfterKNegations(A=[5,-3,1,2], K = 3))
print(largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 1))