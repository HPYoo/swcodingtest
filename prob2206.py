from collections import deque
N, M = map(int, input().split())
board = [list(map(int,input())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
sx, sy = 0, 0
ax, ay = N - 1, M - 1
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    # 한 번에 갈 수 있는가? 아니면 벽을 부셔야만 갈 수 있는가?
    # 벽을 부수고 가면 더 빨리갈 수 있는가?
    q = deque([[sx, sy, 0]])
    visited[0][0][0] = 1
    while q :
        x, y, brake = q.popleft()
        if x == ax and y == ay : return visited[x][y][brake]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] == 0 and visited[nx][ny][brake] == 0 :
                    visited[nx][ny][brake] = visited[x][y][brake] + 1
                    q.append([nx, ny, brake])
                elif board[nx][ny] == 1 and brake == 0 :
                    visited[nx][ny][brake + 1] = visited[x][y][brake] + 1
                    q.append([nx, ny, brake + 1])
    return -1

print(bfs())