# 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
def bfs():
    visited = [[False for _ in range(w)] for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] != 0 and not visited[i][j] :
                q = [[i, j]]
                visited[i][j] = True
                result += 1
                while q :
                    x, y = q[0]
                    del q[0]
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] :
                            if board[nx][ny] == 1 :
                                visited[nx][ny] = True
                                q.append([nx, ny])
    return result

res = []
while True :
    w, h = map(int, input().split())
    if [w, h] == [0, 0] : break
    board = [list(map(int, input().split())) for _ in range(h)]
    res.append(bfs())

for i in range(len(res)):
    print(res[i])