'''
https://www.geeksforgeeks.org/total-number-of-odd-length-palindrome-sub-sequence-around-each-centre/
'''

# Function to find the total palindromic
# odd Length sub-sequences
def solve(s):
	n = len(s)

	# dp array to store the number of palindromic
	# subsequences for 0 to i-1 and j+1 to n-1
	dp=[[0 for i in range(n)] for i in range(n)]

	# We will start with the largest
	# distance between i and j
	for Len in range(n-1,-1,-1):

		# For each Len, we fix our i
		for i in range(n):

			if i + Len >= n:
				break

			# For this i we will find our j
			j = i + Len

			# Base cases
			if (i == 0 and j == n - 1):
				if (s[i] == s[j]):
					dp[i][j] = 2
				elif (s[i] != s[j]):
					dp[i][j] = 1
			else:
				if (s[i] == s[j]):
					# If the characters are equal
					# then look for out of bound index
					if (i - 1 >= 0):
						dp[i][j] += dp[i - 1][j]

					if (j + 1 <= n - 1):
						dp[i][j] += dp[i][j + 1]

					if (i - 1 < 0 or j + 1 >= n):

						# We have only 1 way that is to
						# just pick these characters
						dp[i][j] += 1

				elif (s[i] != s[j]):

					# If the characters are not equal
					if (i - 1 >= 0):
						dp[i][j] += dp[i - 1][j]

					if (j + 1 <= n - 1):
						dp[i][j] += dp[i][j + 1]

					if (i - 1 >= 0 and j + 1 <= n - 1):

						# Subtract it as we have
						# counted it twice
						dp[i][j] -= dp[i - 1][j + 1]

	ways = []
	for i in range(n):
		if (i == 0 or i == n - 1):

			# We have just 1 palindrome
			# sequence of Length 1
			ways.append(1)
		else:

			# Else total ways would be sum of dp[i-1][i+1],
			# that is number of palindrome sub-sequences
			# from 1 to i-1 + number of palindrome
			# sub-sequences from i+1 to n-1
			total = dp[i - 1][i + 1]
			ways.append(total)

	for i in ways:
		print(i,end=" ")

# Driver code

s = "xyxyx"
solve(s)

# This code is contributed by mohit kumar 29
