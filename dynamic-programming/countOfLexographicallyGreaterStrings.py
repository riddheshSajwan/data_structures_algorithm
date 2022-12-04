'''
Given a string C consisting of lowercase English alphabets of size A.
For each string S of length A, its beauty relative to C is defined as the number of pairs of indices i, j (1 ≤ i ≤ j ≤ A), such that substring S[i..j] is lexicographically larger than substring C[i..j].

Return the count of all possible strings S of length A, such that their beauty relative to C equals exactly B.

Since this count can be very large you are required to return count modulo (109+7).

Problem Constraints
1 <= A <= 2000
0 <= B <= 2000

Input Format
The first argument is an integer A.
The second argument is an integer B.
The third argument is a string C.

Output Format
Return the count of all possible strings of length A, such that their beauty relative to C equals exactly B.

Example Input
Input 1:
 A = 2 
 B = 2
 C = "yz"
Input 2:
 A = 2 
 B = 3
 C = "yx"

Example Output
Output 1:
 26
Output 2:
 2

Example Explanation
Explanation 1:
 All the 26 string "za", "zb", "zc", ..... "zz", beauty relative to C is 2.
Explanation 2:
 There are only 2 strings "zy", "zz" which have beauty 3.
'''