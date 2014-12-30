__author__ = 'Connor'
def isInterleave1(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if s1 == '':
        return s2 == s3
    elif s2 == '':
        return s1 == s3
    else:
        if s3[0] == s1[0]:
            ans1 = isInterleave1(s1[1:],s2,s3[1:])
            if ans1:
                return True
        if s3[0] == s2[0]:
            ans2 = isInterleave1(s1,s2[1:],s3[1:])
            if ans2:
                return True
        else:
            return False

def isInterleave2(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if s1 == '':
        return s2 == s3
    elif s2 == '':
        return s1 == s3
    else:
        res = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        res [0][0] = True
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                res[i+1][0] = True
            else:
                break
        for j in range(len(s2)):
            if s2[j] == s3[j]:
                res[0][j+1] = True
            else:
                break
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s3[i+j+1] and res[i][j+1] == True:
                    res[i+1][j+1] = True
                if s2[j] == s3[i+j+1] and res[i+1][j] == True:
                    res[i+1][j+1] = True
        print(res)
        return res[i+1][j+1]

aa = 'aabcc'
bb = 'dbbca'
s3 = 'aadbbcbcac'
s4 = 'aadbbbaccc'
print(isInterleave2('a','b','ab'))
# print(isInterleave2(aa,bb,s4))