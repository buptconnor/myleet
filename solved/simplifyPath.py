__author__ = 'Connor'
def simplifyPath(path):
    tmp = path.split('/')
    print(tmp)
    paths =[]
    for s in tmp:
        if s=='' or s == '.':
            continue
        elif s == '..':
            if paths != []:
                paths.pop()
        else:
            paths.append(s)
    if paths == []:
        return '/'
    out =''
    for s in paths:
        out += '/'+s

    return out

aa= '/a/./b/../../c/'
aa = '/..//a/b/c/d/../../../..'
ans = simplifyPath(aa)
print(ans)

