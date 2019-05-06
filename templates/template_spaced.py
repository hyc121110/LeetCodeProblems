def solve(a):

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    solve(a)
    
    result = solve(a)

    print(result)