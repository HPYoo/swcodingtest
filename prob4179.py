R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
f_info = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J' :
            sx, sy = i, j
            board[i][j] = '.'
        if board[i][j] == 'F' :
            f_info.append([i, j])

visited = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def fire():
    size = len(f_info)
    for f in range(size):
        x, y = f_info[f]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.' :
                board[nx][ny] = 'F'
                f_info.append([nx, ny])
    del f_info[:size]

def jihun():
    q = [[sx, sy]]
    visited[sx][sy] = 1
    fire()
    while q :
        qsize = len(q)
        for it in range(qsize):
            x, y = q[it]
            if x == 0 or x == R - 1 or y == 0 or y == C - 1 :
                return visited[x][y]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] == '.' :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
        del q[:qsize]
        fire()
    return "IMPOSSIBLE"

print(jihun())