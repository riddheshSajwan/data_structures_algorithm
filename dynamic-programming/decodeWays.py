'''
https://leetcode.com/problems/decode-ways/
'''
def numDecodings(s):
    if not s or int(s) == 0:
        return 0
    a0 = 1
    a1 = 1 if s[0] != '0' else 0
    a2 = 0
    for i in range(2,len(s)+1):
        a2 = 0
        if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
            a2 += a0
        if s[i-1] != '0':
            a2 += a1
        a0,a1 = a1,a2
    return a2 if len(s) > 1 else a1

print(numDecodings('2101'))
        