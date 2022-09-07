n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(10001)]
dp[1] = arr[1]
if n > 1 :
    dp[2] = dp[1] + arr[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i-1], dp[i-3] + arr[i -1] + arr[i], dp[i-2] + arr[i])

print(dp[n])

# 정리하고 식 세우는 습관 필요