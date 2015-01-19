__author__ = 'Connor'

# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        ans = []
        sort_can = sorted(candidates)
        if target<sort_can[0]:
            return []
        if target in candidates:
            ans.append([target])
        i = 0
        while i < len(sort_can):
            if target < sort_can[i]:
                break

            res =self.combinationSum(candidates,target-sort_can[i])
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
    candidate_set = [2,3,6,7]
    ans = so.combinationSum(candidate_set,7)
    print(ans)