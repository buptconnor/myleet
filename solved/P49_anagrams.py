__author__ = 'Connor'
#易位构词游戏
def anagrams(strs):
    dict = {}
    ans =[]
    for i in strs:
        sortedwrd = ''.join(sorted(i))
        if sortedwrd not in dict:
            dict[sortedwrd] = [i]
        else:
            dict[sortedwrd].append(i)

    for item in dict.keys():
        if len(dict[item])>=2:
            ans +=dict[item]

    return ans
    # for j in strs[i]:
    #     if j not in dict[i].keys():
    #         dict[i][j] = 1
    #     else:
    #         dict[i][j] += 1
    # for j in range(len(strs)):
    #     if check(ans,strs[j]):
    #         continue
    #     tmp = [strs[j]]
    #     k = j+1
    #     while k<len(strs):
    #         if dict[j] == dict[k]:
    #             tmp.append(strs[k])
    #         k += 1
    #     if len(tmp)>1:
    #         ans.append(tmp)
    # return ans

def check(ans,s):
    for ll in ans:
        if s in ll:
            return True
    return False


aa ='tea'
print(''.join(sorted(aa)))
inputs = ["tea","and","ate","eat","den"]
ans = anagrams(inputs)
print(ans)