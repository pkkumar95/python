def alignment(str1, str2, x, y, dp):
    temp1 = []
    temp2 = []

    i = x
    j = y

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            temp1.append(str1[i - 1])
            temp2.append(str2[j - 1])
            i = i - 1
            j = j - 1
        else:
            minimum = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
            if minimum == dp[i][j - 1]:
                temp1.append('-')
                temp2.append(str2[j - 1])
                j = j - 1
            elif minimum == dp[i - 1][j]:
                temp1.append(str1[i - 1])
                temp2.append('-')
                i = i - 1
            else:
                temp1.append(str1[i - 1])
                temp2.append(str2[j - 1])
                i = i - 1
                j = j - 1

    temp1.reverse()
    temp2.reverse()

    print(temp1)
    print(temp2)

def editDistDP(str1, str2, m, n):
	dp = [[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i][j-1],
								dp[i-1][j],
								dp[i-1][j-1])

	alignment(str1, str2, m, n, dp)

	return dp[m][n]

str1 = input()
str2 = input()

print(editDistDP(str1, str2, len(str1), len(str2)))
