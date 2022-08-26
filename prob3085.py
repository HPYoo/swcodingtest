N = int(input())
board = [list(map(str, input())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_combination(arr):
    temp = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] :
                    if arr[i][j] != arr[nx][ny] :
                        temp.append([[i, j], [nx, ny]])
    return temp

def countcandy(arr, combination):
    x1, y1 = combination[0]
    x2, y2 = combination[1]
    # Change each other
    arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]
    # Count Candy : 'C', 'P', 'Z', 'Y'
    # 행 기준으로 파악
    maxValue = 0
    for i in range(N):
        max_candy = 1
        char = arr[i][0]
        for j in range(1, N):
            if char != arr[i][j] :
                max_candy = 1
                char = arr[i][j]
            else :
                max_candy += 1
            maxValue = max(maxValue, max_candy)
    # 열 기준으로 파악
    for j in range(N):
        max_candy = 1
        char = arr[0][j]
        for i in range(1, N):
            if char != arr[i][j] :
                max_candy = 1
                char = arr[i][j]
            else :
                max_candy += 1
            maxValue = max(maxValue, max_candy)
    arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]
    return maxValue

comb = find_combination(board)

result = 0
for features in range(len(comb)):
    cnt = countcandy(board, comb[features])
    result = max(result, cnt)

print(result)