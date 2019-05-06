def selfDividingNumbers(left, right):
    # naive solution
    res = []
    while left <= right:
        scan = True
        l_str = str(left)
        if left < 10:
            res.append(left)
            left += 1
            continue
        for i in range(len(l_str)):
            if l_str[i] == '0':
                scan = False
                break
            if left % int(l_str[i]) != 0:
                scan = False
                break
        if scan:
            res.append(left)
        left += 1
    return res
    # 2 liner
    # return [x for x in range(left, right+1) if all((i and (x % i==0) for i in map(int, str(x))))]

print(selfDividingNumbers(left=1,right=22))