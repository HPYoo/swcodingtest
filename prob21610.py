N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
water_info = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
ds_info = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def moveNrain():
    temp = []
    di, si = ds_info[0]
    del ds_info[0]
    while water_info :
        x, y = water_info[0]
        del water_info[0]
        nx = x + si * dx[di]
        ny = y + si * dy[di]
        while nx < 0 : nx += N
        while nx >= N : nx -= N
        while ny < 0 : ny += N
        while ny >= N : ny -= N
        board[nx][ny] += 1
        visited[nx][ny] = True
        temp.append([nx, ny])
    return temp

def copybug():
    while water_info :
        x, y = water_info[0]
        del water_info[0]
        cnt = 0
        for d in [2, 4, 6, 8] :
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0 :
                cnt += 1
        board[x][y] += cnt

def cloud():
    temp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and not visited[i][j] :
                board[i][j] -= 2
                temp.append([i, j])
    return temp

it = 0
while it < M :
    visited = [[False for _ in range(N)] for _ in range(N)]
    water_info = moveNrain()
    water_info = copybug()
    water_info = cloud()
    it += 1
result = 0
for i in range(N) :
    result += sum(board[i])

print(result)