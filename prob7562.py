from collections import deque
test_case = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상상우, 우우상, 우우하, 하하우, 하하좌, 좌좌하, 좌좌상, 상상좌
k_path = [[0, 0, 3], [3, 3, 0], [3, 3, 1], [1, 1, 3], [1, 1, 2], [2, 2, 1], [2, 2, 0], [0, 0, 2]]
result = []
for test in range(test_case):
    N = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([[sx, sy, 0]])
    visited[sx][sy] = True
    if sx == ax and sx == ay :
        result.append(0)
    else :
        while q :
            x, y, cnt = q.popleft()
            if x == ax and y == ay :
                result.append(cnt)
                break
            for path in k_path :
                nx = x + dx[path[0]] + dx[path[1]] + dx[path[2]]
                ny = y + dy[path[0]] + dy[path[1]] + dy[path[2]]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt + 1])

for i in range(test_case):
    print(result[i])
