'''
Problem Description

Given an integer A which denotes the number of people standing in the queue.

A selection process follows a rule where people standing on even positions are selected. Of the selected people a queue is formed and again out of these only people on even position are selected.

This continues until we are left with one person. Find and return the position of that person in the original queue.



Problem Constraints
1 <= A <= 109



Input Format
The only argument given is integer A.



Output Format
Return the position of the last selected person in the original queue.
'''

def solve(A):
    exp = 0
    while A > 1:
        A //= 2
        exp += 1
    return 2**exp

print(solve(10))
        
            