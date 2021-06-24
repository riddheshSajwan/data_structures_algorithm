def permute(S):
    result = []
    
    if not S:
        return []
    elif len(S) == 1:
        return [S]
    elif len(S) == 2:
        result = result + [S,S[::-1]]
    else:
        for i in range(len(S)):
            perms = permute(S[:i]+S[i+1:])
            for perm in perms:
                result = result + [[S[i]]+perm]
    
    return result

print(permute([1,2,3]))