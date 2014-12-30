__author__ = 'Connor'
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def printinterval(ii):
    for i in ii:
        print('['+str(i.start)+','+str(i.end)+']')

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
def insert(intervals, newInterval):
    if intervals == []:
        return [newInterval]
    tmp = sorted(intervals,key = lambda intervals:intervals.start)
    # printinterval(tmp)
    i = 0

    if newInterval.end < tmp[0].start:
        ans = [newInterval]
        ans.extend(tmp)
        return ans
    end = 0
    while i < len(intervals):
        if tmp[i].end < newInterval.start:
            i += 1
            continue
        else:
            if tmp[i].start > newInterval.end:
                ans = tmp[0:i]
                ans.append(newInterval)
                ans.extend(tmp[i:])
                return ans
            tmp[i] = Interval(min(tmp[i].start,newInterval.start),max(tmp[i].end,newInterval.end))
            j = i+1
            end = i
            while j < len(tmp):
                if tmp[j].start <= tmp[i].end:
                    tmp[i] = Interval(tmp[i].start,max(tmp[i].end,tmp[j].end))
                else:
                    tmp[end + 1] = tmp[j]
                    end += 1
                j += 1
            return tmp[0:end+1]
    tmp.append(newInterval)
    return tmp



aa =[[1,2],[3,5],[6,7],[9,10],[12,16]]

bb =[]
for i in aa:
    bb.append(Interval(i[0],i[1]))
toInsert = Interval(0,1)
# ans should be [1,2],[3,10],[12,16]
ans = insert(bb,toInsert)
printinterval(ans)