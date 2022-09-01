from collections import deque
N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
land_info = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L' :
            land_info.append([i, j])
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# Find Continent
def solve():
    maxValue = 0
    while land_info :
        x, y = land_info.popleft()
        q = deque([[x, y, 0]])
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[x][y] = True
        while q :
            x, y, cnt = q.popleft()
            maxValue = max(maxValue, cnt)
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                    if board[nx][ny] == "L" :
                        visited[nx][ny] = True
                        q.append([nx, ny, cnt + 1])
    print(maxValue)

solve()