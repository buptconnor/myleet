__author__ = 'Connor'
def compareVersion(version1, version2):
    if version1 == version2:
        return 0
    tmp1 = version1.split('.')
    tmp2 = version2.split('.')
    longer = 0
    if len(tmp1)> len(tmp2):
        length = len(tmp2)
        longer = 1
    elif len(tmp1)<len(tmp2):
        length = len(tmp1)
        longer = 2
    else:
        length = len(tmp1)
    # length = min(len(tmp1),len(tmp2))
    i = 0
    while i < length:
        if int(tmp1[i])>int(tmp2[i]):
            return 1
        elif int(tmp1[i])<int(tmp2[i]):
            return -1
        i +=1
    if longer == 1:
        if int(tmp1[i]) != 0:
            return 1
    elif longer == 2:
        if int(tmp2[i]) != 0:
            return -1
    return 0

v1 = '01'
v2 = '1.0'
ans = compareVersion(v1,v2)
print(ans)