'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''
def minRemoveToMakeValid(s):
      s = list(s)
      stack = []
      for i, char in enumerate(s):
          if char == '(':
              stack.append(i)
          elif char == ')':
              if stack:
                  stack.pop()
              else:
                  s[i] = ''
      while stack:
          s[stack.pop()] = ''
      return ''.join(s)

print(minRemoveToMakeValid('lee(t(c)o)de)'))

def minRemoveToMakeValid2(s):
    open = 0
    i = 0
    toDelete = []
    for i in range(len(s)):
        if s[i] == '(':
            open += 1
            toDelete.append(i)
        elif s[i] == ')':
            if open > 0:
                toDelete.pop()
            open -= 1  
            if open < 0:
                toDelete.append(i)
                open = 0
    
    if toDelete:
        newS = ""
        prevIndex = 0
        for index in toDelete:
            newS += s[prevIndex:index]
            prevIndex = index+1
            newS += s[prevIndex:]
            return newS          
    return s
      
print(minRemoveToMakeValid2('lee(t(c)o)de)'))