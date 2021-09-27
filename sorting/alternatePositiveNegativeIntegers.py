'''
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
'''
def solve(A):
    neg = []
    pos = []
    for item in A:
        if item >= 0:
            pos.append(item)
        else:
            neg.append(item)
    A.clear()
    i,j = 0,0
    while i < len(neg) and j < len(pos):
        A.append(neg[i])
        A.append(pos[j])
        i += 1
        j += 1
    if i < len(neg):
        A += neg[i:]
    if j < len(pos):
        A += pos[j:]
    return A

print(solve([5, -17, -100, -11]))