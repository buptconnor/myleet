__author__ = 'Connor'
def strStr( haystack, needle):
    if needle == '':
        return 0
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0] and i <= len(haystack) - len(needle):
            j =1
            nextstart = 1
            flag = True
            while j < len(needle) :
                if haystack[i+j] == needle[0] and haystack[i+1] != needle[0] and nextstart == 1 :
                        nextstart = j
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
                else:
                    j +=1
            if flag:
                return i
            else:
                i += nextstart
        else:
            i += 1
    return -1


s1 = 'babbbbbabb'#'this test is teta test'
s2 ='bbab' #'test'
ans = strStr(s1,s2)
print(ans)

