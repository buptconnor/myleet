__author__ = 'Connor'
def longestValidParentheses(s):
    le =0
    ri = 0
    maxlen = 0
    for i in range(len(s)):
        if s[i] == '(':
             le +=1
             #maxlen=max(maxlen,2*min(le,ri))
        else:
            if le == ri:
                maxlen=max(maxlen,2*min(le,ri))
                le = 0
                ri = 0
            else:
                ri += 1
    if ri == le :
        return max(maxlen,2*ri)
    if ri != 0:
        j = i
        rr = 0
        ll = 0
        while j > i-ri-le:
            if s[j] == ')':
                rr +=1
            else:
                if rr == ll:
                    maxlen=max(maxlen,2*min(ll,rr))
                    ll = 0
                    rr = 0
                else:
                    ll +=1
            j -=1
        maxlen = max(maxlen,2*min(ll,rr))

    return maxlen

def test(s):
    maxlen=0
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)


ss = ')()((())(()()()'
ans = longestValidParentheses(ss)
print(ans)