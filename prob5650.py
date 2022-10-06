def block(block_num, d):
    if block_num == 1 :
        ref_d = [3, 2, 0, 1]
    if block_num == 2 :
        ref_d = [2, 0, 3, 1]
    if block_num == 3 :
        ref_d = [2, 3, 1, 0]
    if block_num == 4 :
        ref_d = [1, 3, 0, 2]
    if block_num == 5 :
        ref_d = [2, 3, 0, 1]
    return ref_d[d]

def warmhole(hole_num, x, y):
    [x1, y1], [x2, y2] = h_info[hole_num]
    if [x, y] == [x1, y1] :
        return x2, y2
    if [x, y] == [x2, y2] :
        return x1, y1

def move(x, y, sx, sy, d):
    global result
    cnt = 0
    while True :
        x += dx[d]
        y += dy[d]
        if [x, y] == [sx, sy] : break
        if x < 0 or x >= N or y < 0 or y >= N :
            d = block(5, d)
            cnt += 1
            continue
        if 0 <= x < N and 0 <= y < N :
            if 1 <= board[x][y] <= 5 :
                d = block(board[x][y], d)
                cnt += 1
                continue
            if 6 <= board[x][y] <= 10 :
                x, y = warmhole(board[x][y], x, y)
                continue
            if board[x][y] == -1 :
                break
    result = max(result, cnt)

def solve():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 :
                for direction in range(4):
                    move(i, j, i, j, direction)

T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    h_info = {6 : [], 7 : [], 8 : [], 9 : [], 10 : []}
    result = 0
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10 :
                h_info[board[i][j]].append([i, j])

    # 하, 좌, 상, 우
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    solve()
    print('#{}'.format(str(tc+1) + ' ' + str(result)))