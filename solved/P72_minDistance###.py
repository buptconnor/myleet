def minDistance(word1,word2):
    if len(word1) >= len(word2):
        long = word1
        short = word2
    else:
        long = word2
        short = word1
    dif = len(long)-len(short)
    minD = len(long)
    ll = len(long)
    ls = len(short)
    i = 0
    while i <= dif:
        assembled = long[0:i]+short+long[i+ls:ll]
        print(i)
        print(assembled)
        print(long)
        newD = wordDis(long,assembled)
        print(newD)
        minD = min(newD+dif,minD)
        i += 1
    long += long
    print(long)
    print(len(long))
    while i <= ll*2-ls:
        assembled = long[0:i]+short+long[i+ls:ll*2]
        print('num:'+str(i))
        print(assembled)
        print(long)
        newD = wordDis(long,assembled)
        print(newD+i)
        minD = min(newD+i,minD)
        i += 1
    return minD
def wordDis(w1,w2):
    dis = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            dis +=1
    return dis

def test(word1,word2):
    l1 = len(word1)
    l2 = len(word2)
    dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
    for i in range(l1 + 1):
        dp[i][0] = i
    for i in range(l2 + 1):
        dp[0][i] = i
    print(dp)
    for i in  range(1,l1+1):
        for j in range(1,l2+1):
            newD = dp[i-1][j-1]
            if word1[i-1] != word2[j-1]:
                newD += 1
            dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,newD)
    print(dp)
    return dp[l1][l2]

def test2(word1,word2):
    m=len(word1)+1; n=len(word2)+1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i]=i
    for i in range(m):
        dp[i][0]=i
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))

    return dp[m-1][n-1]

def minDist(str1,str2):
    M = len(str1) + 1
    N = len(str2) + 1
    dp = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        dp[i][0] = i
    for j in range(N):
        dp[0][j] = j
    for i in range(1,M):
        for j in range(1,N):
            dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1] + (0 if str1[i-1] == str2[j-1] else 1))



    return dp[M-1][N-1]



a = "horse"
b =  "ros"
# ans = minDistance(a,b)
# print(ans)
print(minDist(a,b))