'''
https://leetcode.com/problems/maximum-frequency-stack/
'''

def solve(A):
    max_freq = float('-inf')
    freq_map = {}
    stack_map = {}
    res = []
    for item in A:
        action = item[0]
        element = item[1]
        if action == 1:
            if element not in freq_map:
                freq_map[element] = 0
            freq_map[element] += 1
            max_freq = max(max_freq,freq_map[element])
            if freq_map[element] not in stack_map:
                stack_map[freq_map[element]] = []
            stack_map[freq_map[element]].append(element)
            res.append(-1)    
        else:
            freq_map[stack_map[max_freq][-1]] -= 1
            res.append(stack_map[max_freq].pop())
            if stack_map[max_freq] == []: max_freq -= 1
    return res

A = [
        [1, 5],
        [1, 7],
        [1, 5],
        [1, 7],
        [1, 4],
        [1, 5],
        [2, 0],
        [2, 0],
        [2, 0],
        [2, 0]  ]

print(solve(A))
