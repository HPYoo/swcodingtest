N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
calc_info = [list(map(int, input().split())) for _ in range(T)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn(xi, di, ki):
    # xi 의 배수가 되는 원판을 di 방향으로 ki 번 돌린다.
    itk = 1
    it = itk * xi
    while it -1 < len(board):
        temp = board[it-1].copy()
        for _ in range(ki):
            if di == 0 : # 시계 방향
                temp.insert(0, temp[-1])
                del temp[-1]
            else : # 반시계방향
                temp.append(temp[0])
                del temp[0]
        # 다 돌렸다
        for i in range(M):
            board[it -1][i] = temp[i]
        itk += 1
        it = itk * xi

def adjacent() :
    temp = []
    ni, mi= [-1, 1], [-1, 1]
    for i in range(N):
        for j in range(M):
            # choose 1 point
            if board[i][j] != 'X':
                x, y = i, j
                num = board[x][y]
                # 자기 자신을 기준으로 탐색
                for my in range(2) :
                    nx = x
                    ny = y + mi[my]
                    while ny >= M : ny -= M
                    while ny < 0 : ny += M
                    if num == board[nx][ny] :
                        temp.append([nx, ny])
                # 원판끼리 탐색
                for nx in range(2) :
                    nx = x + ni[nx]
                    ny = y
                    if 0 <= nx < N :
                        if num == board[nx][ny] :
                            temp.append([nx, ny])
    if temp :
        for x, y in temp :
            board[x][y] = 'X'
    else :
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 'X' :
                    total += board[i][j]
                    cnt += 1
        if cnt > 0 :
            average = total / cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j] != 'X':
                        if board[i][j] < average :
                            board[i][j] += 1
                        elif board[i][j] > average :
                            board[i][j] -= 1

def solve() :
    for x, d, k in calc_info :
        turn(x, d, k)
        adjacent()
    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 'X':
                result += board[i][j]
    print(result)

solve()