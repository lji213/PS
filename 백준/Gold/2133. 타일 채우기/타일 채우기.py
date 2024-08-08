n = int(input())

dp = [[0,0,1,1,0], [1,1,0,0,3]]+[[0,0,0,0,0] for _ in range(n-2)]

for i in range(2, n):
    dp[i][0] = dp[i-1][2]   
    dp[i][1] = dp[i-1][3]
    dp[i][2] = dp[i-1][1]+dp[i-1][4]
    dp[i][3] = dp[i-1][0]+dp[i-1][4]
    dp[i][4] = dp[i][0]+dp[i][1]+dp[i-2][4]

print(dp[n-1][4])