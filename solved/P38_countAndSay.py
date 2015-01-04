__author__ = 'Connor'
def countAndSay(n):
    if n <= 0:
        return ''
    if n == 1:
        return '1'
    seq = countAndSay(n-1)
    ans = ''
    i=0
    while i < len(seq):
        num = seq[i]
        cnt = 1
        while i+cnt <len(seq) and seq[i+cnt] ==num:
            cnt += 1
        ans += str(cnt)+num
        i += cnt
    return ans

ans = countAndSay(6)
print(ans)