R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
w_info = []
sx, sy = 0, 0
ex, ey = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            w_info.append([i, j])
        elif board[i][j] == 'D' :
            ex, ey = i, j
            board[i][j] = '.'
        elif board[i][j] == 'S' :
            sx, sy = i, j
            board[i][j] = '.'

def wateriscoming():
    size = len(w_info)
    for i in range(size):
        x, y = w_info[i][0], w_info[i][1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C :
                if nx == ex and ny == ey :
                    continue
                if board[nx][ny] == '.' :
                    board[nx][ny] = '*'
                    w_info.append([nx, ny])
    del w_info[:size]

def beaverexodus():
    q = [[sx, sy]]
    visited[sx][sy] = 0
    wateriscoming()
    while q :
        qsize = len(q)
        for j in range(qsize):
            x, y = q[j][0], q[j][1]
            if x == ex and y == ey :
                return visited[x][y]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] == '.' :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
        del q[:qsize]
        wateriscoming()
    return "KAKTUS"

print(beaverexodus())