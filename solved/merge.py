__author__ = 'Connor'
from operator import itemgetter

#given a collection of intervals, merge all overlapping intervals.
class interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    tmp = sorted(intervals,key = lambda intervals:intervals[1])
    i = 1
    end = 0
    while i <len(tmp):
        j = 0
        newend = Noneone
        while j <= end:
            ifcovered = overlap(tmp[j],tmp[i])
            if ifcovered != Falsealse:
                tmp[j] = ifcovered
                newend = j
            j +=1

        if newend != None :
            end = newend
        else:
            tmp[end+1] = tmp[i]
            end += 1
        i += 1
    print(end)
    return tmp[0:end+1]

def overlap(line1,line2):
    if line1[1]>=line2[0]:
        start = min(line1[0],line2[0])
        return [start,line2[1]]
    else:
        return False

def printinterval(ii):
    for i in ii:
        print('['+str(i.start)+','+str(i.end)+']')
def test(intervals):
    tmp = sorted(intervals,key = lambda intervals:intervals.end)
    i = 1
    end = 0
    # printinterval(tmp)
    while i < len(tmp):
        j = 0
        newend = None
        while j <= end :
            ifcovered = overlap2(tmp[j],tmp[i])
            if ifcovered != False:
                tmp[j] = ifcovered
                newend = j
            j += 1

        if newend != None:
            end =newend
        else:
            tmp[end+1] = tmp[i]
            end += 1
        i +=1
    return tmp[0:end+1]

def overlap2(interval1,interval2):
    if interval1.end>=interval2.start:
        start = min(interval1.start,interval2.end)
        return interval(start,interval2.end)
    else:
        return False

def test2(intervals):
    tmp = sorted(intervals,key = lambda intervals:intervals.start)
    # printinterval(tmp)
    i =1
    end = 0
    while i < len(intervals):
        j = end
        if tmp[i].start <= tmp[j].end:
            tmp[j]=interval(tmp[j].start,max(tmp[j].end,tmp[i].end))
        else:
            end += 1
            tmp[end] = tmp[i]
        i += 1
    return tmp[0:end+1]



aa =[[1,3],[2,6],[3,4],[8,10],[15,18]]
bb =[]
for i in aa:
    bb.append(interval(i[0],i[1]))
# print(bb)
# printinterval(bb)
# ans =merge(aa)
# print(ans)
ans = test2(bb)
printinterval(ans)
