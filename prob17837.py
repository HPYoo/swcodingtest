N, K = map(int, input().split()) # 풀이 시간 120min
board = [list(map(int, input().split())) for _ in range(N)]
k_info = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    k_info[i][0] -= 1
    k_info[i][1] -= 1
    k_info[i][2] -= 1

new_board = [[[] for _ in range(N)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def change(direction):
    if direction == 0 : direction = 1
    elif direction == 1 : direction = 0
    elif direction == 2 : direction = 3
    else : direction = 2
    return direction
def solve():
    for i, (x, y, _) in enumerate(k_info) :
        new_board[x][y].append(i)
    result = 0
    while True :
        for i in range(K) :
            blue_cnt = 0
            check = False
            x, y, d = k_info[i]
            while True :
                nx = x + dx[d]
                ny = y + dy[d]
                # 파란색 판
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2 :
                    blue_cnt += 1
                    if blue_cnt == 2 :
                        break
                    else :
                        d = change(d)
                        k_info[i][2] = d
                        continue
                elif 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0 :
                        k_info[i][0], k_info[i][1] = nx, ny
                        # 이 놈 위에 있는 녀석 한꺼번에 이동시키자.
                        tmp = new_board[x][y][new_board[x][y].index(i): ]
                        for j in range(len(tmp)):
                            new_board[nx][ny].append(tmp[j])
                            k_info[tmp[j]][0], k_info[tmp[j]][1] = nx, ny
                        del new_board[x][y][new_board[x][y].index(i):]
                        break
                    if board[nx][ny] == 1 :
                        k_info[i][0], k_info[i][1] = nx, ny
                        tmp = new_board[x][y][new_board[x][y].index(i):]
                        # 반대로 뒤집자
                        filp = []
                        for j in range(len(tmp)-1, -1, -1):
                            filp.append(tmp[j])
                        for j in range(len(filp)):
                            new_board[nx][ny].append(filp[j])
                            k_info[filp[j]][0], k_info[filp[j]][1] = nx, ny
                        del new_board[x][y][new_board[x][y].index(i):]
                        break
            # 검사하자
            for xi in range(N):
                for yj in range(N):
                    if len(new_board[xi][yj]) >= 4 :
                        check = True
                        break
                if check == True :
                    break
            if check == True :
                break
        result += 1
        if check == True :
            break
        if result > 1000: break
    return result

time = solve()
if time > 1000 : print(-1)
else : print(time)