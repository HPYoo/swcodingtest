M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

def solve():
    maxValue = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if board[i-1][j-1] == 0 :
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxValue = max(maxValue, dp[i][j])
    return maxValue

print(solve())