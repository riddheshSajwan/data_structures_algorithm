'''
https://www.algoexpert.io/questions/Validate%20Subsequence
'''
def isValidSubsequence(array, sequence):
    # Write your code here.
	cache = set()
	index = 0
	if sequence == array:
		return True
	elif len(sequence) > len(array):
		return False
	for num in array:
		if index == len(sequence):
			return True
		if sequence[index] in cache:
			return False
		if num == sequence[index]:
			index += 1
		else:
			cache.add(num)
	return index == len(sequence)
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

# best solution
def isValidSubsequence2(array, sequence):
    # Write your code here.
    seqIdx=0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
print(isValidSubsequence2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))