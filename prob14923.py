# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:11:14 2022

@author: user
"""

from collections import deque
N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
hx, hy, ex, ey = hx - 1, hy - 1, ex - 1, ey - 1
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y, 0, 1]) # x, y, cnt, magic 남은 횟수
    visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
    # x, y 위치에서 magic이 한 번 쓸 수 있는 상태로 있는 것이기 때문에
    # visited의 3번째 인덱스는 1
    visited[x][y][1] = True
    while q :
        x, y, cnt, magic = q.popleft()
        if x == ex and y == ey :
            return cnt # 목적지에 도달하였다면 cnt 출력
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny][magic] : # 이미 방문한 곳은 카운팅할 필요가 없다.
                    continue
                if board[nx][ny] == 1 and magic == 1 : #  벽인데 마법 아직 안씀
                    visited[nx][ny][0] = True # 마법을 쓴다.
                    q.append([nx, ny, cnt + 1, magic - 1])
                elif board[nx][ny] == 0 : # 그냥 길
                    visited[nx][ny][magic] = True # 마법 쓸필요없음
                    q.append([nx, ny, cnt + 1, magic])
    return -1 # 이래저래 했는데 도달하지 못했을때!

print(bfs(hx, hy))

