N, M, K = map(int, input().split())
f_info = []
for i in range(M):
    temp = list(map(int, input().split()))
    f_info.append([temp[0]-1, temp[1]-1, temp[2], temp[3], temp[4]])

board = [[[] for _ in range(N)] for _ in range(N)]

# 상, 상우, 우, 우하, 하, 하좌, 좌, 좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    while f_info :
        x, y, m, s, d = f_info[0]
        del f_info[0]
        nx = x + s * dx[d]
        ny = y + s * dy[d]
        while nx < 0 : nx += N
        while nx >= N : nx -= N
        while ny < 0 :  ny += N
        while ny >= N : ny -= N
        board[nx][ny].append([m, s, d])

def divide():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 1 :
                f_info.append([i, j, board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]])
                board[i][j] = []
            if len(board[i][j]) > 1 :
                dm, ds, dd = 0, 0, []
                for k in range(len(board[i][j])):
                    dm += board[i][j][k][0]
                    ds += board[i][j][k][1]
                    dd.append(board[i][j][k][2])
                check = dd[0] % 2
                new_dd = [0, 2, 4, 6]
                for k in range(1, len(dd)):
                    if check != dd[k] % 2 :
                        new_dd = [1, 3, 5, 7]
                        break
                dm //= 5
                ds //= len(board[i][j])
                if dm != 0 :
                    for k in range(4):
                        f_info.append([i, j, dm, ds, new_dd[k]])
                board[i][j] = []

def solve():
    it = 0
    result = 0
    while it < K :
        move()
        divide()
        it += 1
    for i in range(len(f_info)):
        result += f_info[i][2]
    return result
print(solve())