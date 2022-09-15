N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dice_row = [4, 1, 3, 6]
dice_col = [2, 1, 5, 6]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 주사위 굴리기 매커니즘
def roll(d):
    # 동, 서
    if d == 1 :
        dice_row.insert(0, dice_row[-1])
        del dice_row[-1]
        dice_col[-1] = dice_row[-1]
        dice_col[1] = dice_row[1]
    if d == 3 :
        dice_row.append(dice_row[0])
        del dice_row[0]
        dice_col[-1] = dice_row[-1]
        dice_col[1] = dice_row[1]
    # 남, 북
    if d == 0 :
        dice_col.append(dice_col[0])
        del dice_col[0]
        dice_row[-1] = dice_col[-1]
        dice_row[1] = dice_col[1]
    if d == 2 :
        dice_col.insert(0, dice_col[-1])
        del dice_col[-1]
        dice_row[-1] = dice_col[-1]
        dice_row[1] = dice_col[1]

def rotate(a, b, d) :
    if a > b :
        return (d + 1) % 4
    if a < b :
        return (d - 1) % 4
    if a == b :
        return d

def reverse(d):
    d += 2
    if d == 5 :
        d = 1
    if d == 4 :
        d = 0
    return d
# 주사위 최족 도착 위치에서 점수 얻기
def bfs(x, y):
    q = [[x, y]]
    B = board[x][y]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True
    cnt = 1
    while q :
        x, y = q[0]
        del q[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                if board[nx][ny] == B :
                    visited[nx][ny] = True
                    cnt += 1
                    q.append([nx, ny])
    return cnt * B

def solve():
    x, y, d = 0, 0, 1
    score = 0
    it = 0
    while True :
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            d = reverse(d)
            continue
        else :
            roll(d)
            score += bfs(nx, ny)
            d = rotate(dice_row[-1], board[nx][ny], d)
            x, y = nx, ny
            it += 1
        if it == K : break
    return score

print(solve())