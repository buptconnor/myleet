__author__ = 'Connor'
def restoreIpAddresses(s):
    ans = []
    pts = [1,2,3]
    length = len(s)
    if length > 12:
        return ans
    while pts[0] < length:
        pts [1] = pts[0]+1
        while pts[1] < pts[2]:
            pts [2] = pts[1]+1
            while pts[2] < len(s):
                if ( pts[0]<=3 and (pts[1]-pts[0])<=3 and (pts[2]-pts[1])<=3):
                    Flag = True
                    ips = [s[0:pts[0]],s[pts[0]:pts[1]],s[pts[1]:pts[2]],s[pts[2]:]]
                    for i in ips:
                        Flag = int(i)<=255 and Flag
                        if  i[0] == '0':
                            if i != '0':
                                Flag = False
                    if Flag:
                        for i in range(4):
                            ips[i] = str(int(ips[i]))

                        print(ips)
                        ip= '.'.join(ips)
                        if ip not in ans :
                            ans.append(ip)
                pts [2] += 1
            pts[1] += 1
        pts[0] += 1
    return ans

def restoreIpAddresses1( s):
    def dfs(s, sub, ips, ip):
        if sub == 4:                                        # should be 4 parts
            if s == '':
                ips.append(ip[1:])                          # remove first '.'
            return
        for i in range(1, 4):                               # the three ifs' order cannot be changed!
            if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
                if int(s[:i]) <= 255:
                    dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'
    ips = []
    dfs(s, 0, ips, '')
    return ips

aa= '010010'
ans = restoreIpAddresses(aa)
print(ans)
print(restoreIpAddresses1(aa))
