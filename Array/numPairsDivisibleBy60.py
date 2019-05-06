'''
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in
 seconds is divisible by 60.  Formally, we want the number of indices
 i < j with (time[i] + time[j]) % 60 == 0.
'''

from collections import Counter

def numPairsDivisibleBy60(time):
    # naive solution (very slow)
    # res = 0
    # for i in range(len(time)):
    #     for j in range(i+1, len(time)):
    #         if (time[i] + time[j]) % 60 == 0:
    #             res += 1
    # return res

    # better solution (two sum)
    # c = Counter()
    # count = 0
    # for t in time:
    #     count += c[-t % 60] # [-t % 60] storing the complement of the remainder
    #     c[t % 60] += 1 # expecting the complement of the remainder
    # return count

    # faster solution
    dic = collections.defaultdict(int)
    for i in time:
        dic[i%60] += 1
    
    inum = 0
    for key,val in dic.items():
        if key == 30 or key == 0:
            inum += (val*(val-1))//2
        elif key < 60-key and 60-key in dic:
            inum += dic[key]*dic[60-key]
    return inum

print(numPairsDivisibleBy60(time=[30,20,150,100,40]))