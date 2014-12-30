__author__ = 'Connor'
def permute(num):
    if len(num) <= 1:
        return [num]
    ans = []
    for i in num:
        ans = permutenum(ans,i)
    return ans

def permutenum(per,num):
    if per == []:
        return [[num]]
    ans = []
    for i in per:
       ans = merge(ans,insert(i,num))
    return ans

def merge(l1,l2):
    for i in l2:
        if i not in l1:
            l1.append(i)
    return l1


def insert(numl,s):
    ans = []
    for i in range(len(numl)):
        tmp = numl[0:i]
        tmp.append(s)
        tmp.extend(numl[i:])
        if tmp not in ans:
            ans.append(tmp)
    tmp = numl
    tmp.append(s)
    if tmp not in ans :
        ans.append(tmp)
    return ans





    # st = str(num)
    # ans = []
    # for i in range(len(st)):
    #     tmp = int(st[0:i]+str(s)+st[i:])
    #     if tmp not in ans:
    #         ans.append(tmp)
    # tmp = int(st+str(s))
    # if tmp not in ans:
    #     ans.append(tmp)

ss = [1,1,2]
s2 = 4
#ans = insert(ss,s2)
ans = permute(ss)
print(ans)
print(len(ans))