__author__ = 'Connor'
def generateParenthesis(n):
    ans=[]
    if n==0:
        return ans
    gen(ans,'',0,0,n)
    return ans

def gen(ans,s,ln,rn,n):
    if ln==n and rn ==n:
        ans.append(s)
    if ln<n:
        gen(ans,s+'(',ln+1,rn,n)
    if rn<ln and ln<=n:
        gen(ans,s+')',ln,rn+1,n)
    return

aa=generateParenthesis(3)
print(aa)


