N, M, k = map(int, input().split())
board = [[[0, 0] for _ in range(N)] for _ in range(N)] # 상어 번호, 상어 냄새
s_coord = {}
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0 :
            s_coord[tmp[j]] = [i, j]
d_info = list(map(int, input().split()))
d_spec = {}
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    d_spec[i+1] = temp
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def solve():
    time = 0
    while True :
        check_cnt = 0
        for i in range(M):
            if s_coord[i + 1] : # 있는 경우에만 배치
                x, y = s_coord[i + 1]
                if board[x][y][0] != i + 1 and board[x][y][1] == k : # 중복 위치
                    num1, num2 = board[x][y][0], i + 1
                    board[x][y][0] = min(board[x][y][0], i + 1)
                    if num1 < num2 : s_coord[num2] = []
                    else : s_coord[num1] = []
                    check_cnt += 1
                else : board[x][y][0] = i + 1
                board[x][y][1] = k
            else :
                check_cnt += 1
        if M - check_cnt == 1 : break
        if time > 1000 : break
        time += 1
        for i in range(M): # Move
            if s_coord[i + 1] :
                x, y = s_coord[i + 1]
                d_temp = d_spec[i+1][d_info[i]-1] # 이동 규칙 배열
                # 최초 이동 실시
                # 인접한 곳 중 빈 곳 먼저 가자
                cnt = 0
                for d in range(4) :
                    nx = x + dx[d_temp[d]]
                    ny = y + dy[d_temp[d]]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny][1] == 0 :
                        s_coord[i + 1] = [nx, ny]
                        # 방향도 바꿔줘야함
                        d_info[i] = d_temp[d]
                        break
                    else : cnt += 1
                if cnt < 4 :
                    continue
                else :
                    for d in range(4):
                        nx = x + dx[d_temp[d]]
                        ny = y + dy[d_temp[d]]
                        if 0 <= nx < N and 0 <= ny < N and board[nx][ny][0] == i + 1 :
                            s_coord[i + 1] = [nx, ny]
                            d_info[i] = d_temp[d]
                            break
        for i in range(N):
            for j in range(N):
                if board[i][j][1] > 0 :
                    board[i][j][1] = max(board[i][j][1] - 1, 0)
                    if board[i][j][1] == 0 :
                        board[i][j][0] = 0
    return time
result = solve()
if result > 1000 :
    print(-1)
else :
    print(result)


