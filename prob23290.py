M, S = map(int, input().split())
f_info = [list(map(int, input().split())) for _ in range(M)]
board = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
for i in range(len(f_info)):
    f_info[i][0] -= 1
    f_info[i][1] -= 1
    f_info[i][2] -= 1

# 초기조건
for i in range(len(f_info)):
    board[f_info[i][0]][f_info[i][1]].append(f_info[i][2]) # fish
comb = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            comb.append([i, j, k])

# 상, 좌, 하, 우 for shark
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 좌, 좌상, 상, 상우, 우, 우하, 하, 하좌 for fish
fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]
def copy():
    return [arr for arr in f_info]

def move():
    global sx, sy
    # fish
    b_temp = [[[] for _ in range(4)] for _ in range(4)]
    for i, (x, y, d) in enumerate(f_info) :
        cnt = 0
        while True :
            nx = x + fdx[d]
            ny = y + fdy[d]
            if cnt == 8 : break
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 :
                d = (d - 1) % 8
                cnt += 1
                continue
            if 0 <= nx < 4 and 0 <= ny < 4 :
                if smell[nx][ny] > 0 or [nx, ny] == [sx, sy] :
                    d = (d - 1) % 8
                    cnt += 1
                    continue
                elif smell[nx][ny] == 0 :
                    b_temp[nx][ny].append(d)
                    break
        if cnt == 8 :
            b_temp[x][y].append(d)
    # Board Update
    for i in range(4):
        for j in range(4):
            board[i][j] = b_temp[i][j]
    # shark : Count 3, Fish
    temp = {}
    for d1, d2, d3 in comb :
        cnt = 0
        check = True
        x, y = sx, sy
        visited = [[False for _ in range(4)] for _ in range(4)]
        for d in [d1, d2, d3] :
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 :
                check = False
                break
            elif 0 <= nx < 4 and 0 <= ny < 4 :
                if not visited[nx][ny] :
                    if len(board[nx][ny]) >= 1 :
                        cnt += len(board[nx][ny])
                        visited[nx][ny] = True
                    x, y = nx, ny
                else :
                    x, y = nx, ny
        if check :
            try :
                temp[cnt] += [[d1, d2, d3]]
            except :
                temp[cnt] = [[d1, d2, d3]]
        else :
            continue
    maxKey = max(temp)
    x, y = sx, sy
    for d in temp[maxKey][0] :
        nx = x + dx[d]
        ny = y + dy[d]
        if len(board[nx][ny]) >= 1 :
            board[nx][ny] = []
            smell[nx][ny] = 3
        x, y = nx, ny
    sx, sy = nx, ny
    size = len(f_info)
    del f_info[:size]
    for i in range(4):
        for j in range(4):
            if len(board[i][j]) >= 1 :
                for k in range(len(board[i][j])):
                    f_info.append([i, j, board[i][j][k]])

def diminish():
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0 :
                smell[i][j] -= 1

def solve():
    it = 0
    while it < S :
        copy_fish = copy()
        move()
        diminish()
        for x, y, d in copy_fish :
            f_info.append([x, y, d])
            board[x][y].append(d)
        it += 1
    result = 0
    for i in range(4):
        for j in range(4):
            if len(board[i][j]) > 0 :
                result += len(board[i][j])
    print(result)

solve()