from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cheese = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 : cheese.append([i, j])

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 외부 / 치즈
def solve():
    q = deque([[0, 0]])
    visited[0][0][0] = True
    num = len(cheese)
    it = 0
    last_cnt = 0
    while num > 0 :
        temp = []
        cnt = 0
        while q :
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M  :
                    if board[nx][ny] == 0 and not visited[0][nx][ny]:
                        visited[0][nx][ny] = True
                        q.append([nx, ny])
                    if board[nx][ny] == 1 and not visited[1][nx][ny] :
                        temp.append([nx, ny])
                        visited[1][nx][ny] = True
        for x, y in temp :
            board[x][y] = 0
            visited[0][x][y] = True
            cnt += 1
            q.append([x, y])
        last_cnt = num
        num -= cnt
        it += 1
    return [it, last_cnt]

result = solve()
for i in range(2):
    print(result[i])