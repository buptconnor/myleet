__author__ = 'Connor'

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        sorted_num = sorted(num)
        print(sorted_num)
        length = len(num)
        index = [0,1,2]
        ans =[]
        while index[0] < index[1] and index[2] < length:
            while index[1] < index[2] and index[2] < length:
                while index[2] < length:
                    if sorted_num[index[0]] + sorted_num[index[1]] + sorted_num[index[2]] == 0 and [sorted_num[index[0]] , sorted_num[index[1]], sorted_num[index[2]]] not in ans:
                        ans.append([sorted_num[index[0]] , sorted_num[index[1]], sorted_num[index[2]]])
                    index[2] += 1
                index[1] += 1
                index[2] = index[1] + 1
            index[0] += 1
            index[1] = index[0] + 1
            index[2] = index[1] + 1
        return ans
    def test2(self,num):
        sorted_num = sorted(num)
        length = len(num)
        ans = []
        for m in range(length):
            target = 0 - sorted_num[m]
            i = 0
            j = length-1
            while i < j:
                sum2 = sorted_num[i] + sorted_num[j]
                if i == m or j == m:
                    if sum2 <= target:
                        i += 1
                    else:
                        j -= 1
                    continue

                if sum2 == target:
                    tmp =sorted([sorted_num[m], sorted_num[i] , sorted_num[j]])
                    if tmp not in ans:
                        ans.append(tmp)
                    i += 1
                    j -= 1
                elif sum2 < target:
                    while i <length -1 and sorted_num[i] == sorted_num[i+1]:
                        i += 1
                    i += 1
                else:
                    while j>1 and sorted_num[j] == sorted_num[j-1]:
                        j -= 1
                    j -= 1
        return ans

if __name__ == '__main__':
    so = Solution()
    aa = [-1, 0, 1, 2, -1, -4]
    ans = so.threeSum(aa)
    ans2 = so.test2(aa)
    print(ans2)
