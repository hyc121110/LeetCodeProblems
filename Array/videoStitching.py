'''
You are given a series of video clips from a sporting event that lasted T 
seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends 
at time clips[i][1].  We can cut these clips into segments freely: for example, 
a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into 
segments that cover the entire sporting event ([0, T]).  If the task is 
impossible, return -1.
'''

def videoStitching(clips, T):
    clips = sorted(clips)
    start, end = 0, 0
    cnt = 0
    idx = 0
    while start <= end:
        cnt += 1
        newstart, newend = end + 1, end
        # find start
        while idx < len(clips) and start <= clips[idx][0] <= end:
            # keep looking for newend
            newend = max(newend, clips[idx][1])
            if newend >= T:
                # immediately return value
                return cnt
            idx += 1
        # update start and end
        start, end = newstart, newend
    return -1
    
print(videoStitching(clips=[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],
                            [4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T=10))