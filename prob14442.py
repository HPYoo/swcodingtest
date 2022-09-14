import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    q = deque([[0, 0, 0, 1]]) # SX, SY, WALL, CNT
    visited[0][0][0] = True
    while q :
        x, y, wall, cnt = q.popleft()
        if x == N - 1 and y == M - 1 :
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if visited[wall][nx][ny] : continue
                if board[nx][ny] == 0 and not visited[wall][nx][ny] :
                    q.append([nx, ny, wall, cnt + 1])
                    visited[wall][nx][ny] = True
                if board[nx][ny] == 1 and wall < K and not visited[wall+1][nx][ny]: # K 번 이하면 벽을 부술 수 있음
                    visited[wall+1][nx][ny] = True
                    q.append([nx, ny, wall + 1, cnt+1])
    return -1

print(bfs())