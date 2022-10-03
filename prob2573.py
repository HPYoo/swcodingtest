N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited) :
    q = [[x, y]]
    melt_q = []
    visited[x][y] = True
    while q :
        x, y = q[0]
        del q[0]
        melt_cnt = 0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny] :
                if board[nx][ny] != 0 :
                    visited[nx][ny] = True
                    q.append([nx, ny])
                else :
                    melt_cnt += 1
        if melt_cnt :
            melt_q.append([x, y, melt_cnt])
    return melt_q

year = 0
while True :
    count = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visited[i][j] :
                count += 1
                melt = bfs(i, j, visited)
                while melt :
                    mx, my, m = melt[0]
                    del melt[0]
                    board[mx][my] = max(board[mx][my] - m, 0)
    if count == 0 :
        year = 0
        break
    if count >= 2 :
        break
    year += 1
print(year)