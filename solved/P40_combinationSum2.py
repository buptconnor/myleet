__author__ = 'Connor'
import time

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if candidates == []:
            return []
        ans = []
        sort_can = sorted(candidates)
        if target<sort_can[0]:
            return []
        if target in candidates:
            ans.append([target])
        i = 0
        while i<len(sort_can):
            if sort_can[i]> target:
                break
            i += 1
        small_arr = i
        i = 0

        while i < len(sort_can):
            if target < sort_can[i]:
                break
            newcan = []
            newcan.extend(sort_can[0:small_arr])
            newcan.remove(sort_can[i])
            res =self.combinationSum2(newcan,target-sort_can[i])
            for item in res:
                tmp = [sort_can[i]]
                tmp.extend(item)
                tmp = sorted(tmp)
                if tmp not in ans:
                    ans.append(tmp)
            i += 1
        return ans
if __name__ == '__main__':
    so =Solution()
    candidate_set = [13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]#[10,1,2,7,6,1,5]
    t1 = time.clock()
    ans = so.combinationSum2(candidate_set,25)
    t2 = time.clock()
    print(t2-t1)
    print(ans)