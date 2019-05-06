def solve(s):
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = solve(s)

        fptr.write(str(result) + '\n')
        
    fptr.close()