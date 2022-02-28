'''
https://practice.geeksforgeeks.org/problems/binary-string-1587115620/1
'''

def binarySubstring(s):
    #code here
    count = 0
    for item in s:
        if item == '1': count += 1
    return (count*(count-1))//2 # nC2

print(binarySubstring("1111"))


'''
variation - https://www.geeksforgeeks.org/count-substrings-that-starts-with-character-x-and-ends-with-character-y/
'''
