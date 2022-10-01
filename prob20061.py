N = int(input())
info_block_q = [list(map(int, input().split())) for _ in range(N)]

green_board = [[0 for _ in range(4)] for _ in range(6)]
blue_board = [[0 for _ in range(6)] for _ in range(4)]

# 하, 우
dx, dy = [1, 0], [0, 1]
# move
def move(t, x, y) :
    gq = [[t, 0, y]]
    bq = [[t, x, 0]]
    while gq :
        t, x, y = gq[0]
        del gq[0]
        nx = x + dx[0]
        ny = y + dy[0]
        if 0 <= nx < 6 and 0 <= ny < 4 :
            if t == 1 :
                if green_board[nx][ny] == 0 :
                    gq.append([t, nx, ny])
            if t == 2 :
                if green_board[nx][ny] == 0 and green_board[nx][ny + 1] == 0 :
                    gq.append([t, nx, ny])
            if t == 3 and 0 <= nx + 1 < 6 :
                if green_board[nx][ny] == 0 and green_board[nx + 1][ny] == 0 :
                    gq.append([t, nx, ny])
    gx, gy = x, y
    while bq :
        t, x, y = bq[0]
        del bq[0]
        nx = x + dx[1]
        ny = y + dy[1]
        if 0 <= nx < 4 and 0 <= ny < 6 :
            if t == 1 :
                if blue_board[nx][ny] == 0 :
                    bq.append([t, nx, ny])
            if t == 2 and 0 <= ny + 1 < 6 :
                if blue_board[nx][ny] == 0 and blue_board[nx][ny + 1] == 0 :
                    bq.append([t, nx, ny])
            if t == 3 :
                if blue_board[nx][ny] == 0 and blue_board[nx + 1][ny] == 0 :
                    bq.append([t, nx, ny])
    bx, by = x, y
    if t == 1 :
        green_board[gx][gy], blue_board[bx][by] = 1, 1
    if t == 2 :
        green_board[gx][gy], blue_board[bx][by] = 1, 1
        green_board[gx][gy+1], blue_board[bx][by+1] = 1, 1
    if t == 3 :
        green_board[gx][gy], blue_board[bx][by] = 1, 1
        green_board[gx + 1][gy], blue_board[bx + 1][by] = 1, 1

def delete():
    global score
    # 줄 어떻게 지우지
    temp = [[0 for _ in range(4)] for _ in range(6)]
    it = 5
    for i in range(5, -1, -1):
        if green_board[i].count(1) != 4:
            for j in range(4):
                temp[it][j] = green_board[i][j]
            it -= 1
        else : score += 1
    for i in range(6):
        for j in range(4):
            green_board[i][j] = temp[i][j]
    temp = [[0 for _ in range(6)] for _ in range(4)]
    cnt = 0
    it = 5
    for i in range(5, -1, -1):
        for j in range(4):
            if blue_board[j][i] == 1 : cnt += 1
        if cnt != 4 :
            for j in range(4):
                temp[j][it] = blue_board[j][i]
            it -= 1
        else : score += 1
        cnt = 0
    for i in range(4):
        for j in range(6):
            blue_board[i][j] = temp[i][j]

def pastel_delete(num_row, num_col) :
    if num_row != 0 : # green_board
        for i in range(4):
            green_board[-1][i] = 0
        del green_board[-1]
        green_board.insert(0, [0 for _ in range(4)])
        if num_row == 2 :
            for i in range(4):
                green_board[-1][i] = 0
            del green_board[-1]
            green_board.insert(0, [0 for _ in range(4)])
    if num_col != 0 : # blue_board
        for i in range(4):
            del blue_board[i][-1]
            blue_board[i].insert(0, 0)
        if num_col == 2 :
            for i in range(4):
                del blue_board[i][-1]
                blue_board[i].insert(0, 0)

def solve():
    while info_block_q :
        t, x, y = info_block_q[0]
        del info_block_q[0]
        move(t, x, y)
        delete()
        # Green Board count
        row, col = 0, 0
        for i in range(2):
            if green_board[i].count(1) > 0 :
                row += 1
            for j in range(4):
                if blue_board[j][i] != 0 :
                    col += 1
                    break
        pastel_delete(row, col)
    num_tile = 0
    for i in range(6):
        num_tile += green_board[i].count(1)
    for j in range(4):
        num_tile += blue_board[j].count(1)
    return num_tile

score = 0
result = solve()
print(score)
print(result)
# 반례 고려 안하면 냅다 맞았다 하고 낼 거 같은데...