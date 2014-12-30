__author__ = 'Connor'
def letterCombinations(digits):
    dic = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ''
    }
    ans = []
    if '0' in digits or '1' in digits or digits == '':
        return ['']
    for i in range(len(digits)):
        tmp = []
        if ans == []:
            for j in range(len(dic[digits[i]])):
                tmp.append(dic[digits[i]][j])
        else:
            while ans != []:
                pre = ans.pop()
                for j in range(len(dic[digits[i]])):
                    tmp.append(pre+dic[digits[i]][j])
        ans = tmp
    return ans

aa = '234'
res = letterCombinations(aa)
print(res)





