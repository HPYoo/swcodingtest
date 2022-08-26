from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
a1x, a1y = map(int, sys.stdin.readline().split())
a2x, a2y = map(int, sys.stdin.readline().split())
b1x, b1y = map(int, sys.stdin.readline().split())
b2x, b2y = map(int, sys.stdin.readline().split())

def bfs(x, y, gx, gy, visit, path) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    cnt = 0
    visit[x][y] = True
    q.append([x, y, cnt])
    while q :
        x, y, cnt = q.popleft()
        if x == gx and y == gy :
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N and 0 <= ny <= M and not visit[nx][ny] :
                q.append([nx, ny, cnt + 1])
                visit[nx][ny] = True
                path[nx][ny] = [x, y]
    return -1 # 여기까지는 맞음

def get_dist(x1, y1, gx1, gy1, x2, y2, gx2, gy2):
    visited = [[False for _ in range(M + 1)] for _ in range(N + 1)]
    path = [[[0, 0] for _ in range(M + 1)] for _ in range(N + 1)]
    # x1, y1, gx1, gy1 : 먼저 최단거리 결정할 좌표들
    # x2, y2, gx2, gy2 : 그 다음에 거리 찾을 애들, 대신에 미리 방문처리는 해놔야함
    visited[x2][y2] = True
    visited[gx2][gy2] = True
    temp = bfs(x1, y1, gx1, gy1, visited, path)
    # visited 함수 초기화
    visited = [[False for _ in range(M + 1)] for _ in range(N + 1)]
    # x1, y1, gx1, gy1 구간 True 처리
    x, y = gx1, gy1
    # 경로는 하나만 지정해주는 것이 핵심!
    while True :
        visited[x][y] = True
        if x == x1 and y == y1 :
            break
        nx = path[x][y][0]
        ny = path[x][y][1]
        x, y = nx, ny

    temp2 = bfs(x2, y2, gx2, gy2, visited, path)
    return temp, temp2

d1, d2 = get_dist(a1x, a1y, a2x, a2y, b1x, b1y, b2x, b2y)
result = 0
if d1 == -1 or d2 == -1 :
    result = -1
else :
    result = d1 + d2

d1, d2 = get_dist(b1x, b1y, b2x, b2y, a1x, a1y, a2x, a2y)
result2= 0
if d1 == -1 or d2 == -1 :
    result2 = -1
else :
    result2 = d1 + d2

if result == -1 and result2 == -1 :
    print("IMPOSSIBLE")
else :
    if result == -1 : print(result2)
    elif result2 == -1 : print(result)
    else : print(min(result, result2))