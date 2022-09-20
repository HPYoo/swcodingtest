N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def spread(x, y, main_d):
    global result
    dust, total = board[x][y], 0
    # 좌, 상, 하 / 우, 하, 상 / 상, 우, 좌 / 하, 좌, 우 : 메인, 오른쪽(시계방향), 왼쪽(반시계 방향)
    if main_d == 3: # 상, 하, 좌
        direction = [0, 2, 3]
    if main_d == 1: # 하, 상, 우
        direction = [2, 0, 1]
    if main_d == 0: # 우, 좌, 상
        direction = [1, 3, 0]
    if main_d == 2: # 좌, 우, 하
        direction = [3, 1, 2]
    for i, d in enumerate(direction) :
        sx, sy = x, y
        if i == 0 : # 시계방향으로 돌릴때
            ratio = [0.07, 0.1, 0.02, 0.01]
            nx = sx + dx[d]
            ny = sy + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                for j in range(4):
                    result += int(ratio[j] * dust)
                    total += int(ratio[j] * dust)
                continue
            else :
                sx, sy = nx, ny
                board[nx][ny] += int(ratio[0] * dust)
                total += int(ratio[0] * dust)
                sub_d = main_d
                for j in range(1, 4):
                    nx = sx + dx[sub_d]
                    ny = sy + dy[sub_d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N :
                        result += int(ratio[j] * dust)
                        total += int(ratio[j] * dust)
                    else :
                        board[nx][ny] += int(ratio[j] * dust)
                        total += int(ratio[j] * dust)
                    sub_d = (sub_d + 1) % 4
        elif i == 1 : # 반시계방향으로 돌릴때
            ratio = [0.07, 0.1, 0.02, 0.01]
            nx = sx + dx[d]
            ny = sy + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                for j in range(4):
                    result += int(ratio[j] * dust)
                    total += int(ratio[j] * dust)
                continue
            else :
                sx, sy = nx, ny
                board[nx][ny] += int(ratio[0] * dust)
                total += int(ratio[0] * dust)
                sub_d = main_d
                for j in range(1, 4):
                    nx = sx + dx[sub_d]
                    ny = sy + dy[sub_d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N :
                        result += int(ratio[j] * dust)
                        total += int(ratio[j] * dust)
                    else :
                        board[nx][ny] += int(ratio[j] * dust)
                        total += int(ratio[j] * dust)
                    sub_d = (sub_d - 1) % 4
        elif i == 2:
            ratio = [0.05]
            nx = sx + 2 * dx[d]
            ny = sy + 2 * dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                result += int(ratio[0] * dust)
                total += int(ratio[0] * dust)
            else:
                board[nx][ny] += int(ratio[0] * dust)
                total += int(ratio[0] * dust)
            # 이제 진짜 남은 것들만
            remain = dust - total
            nx = sx + dx[d]
            ny = sy + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                result += remain
            else :
                board[nx][ny] += remain
    board[x][y] = 0

stx, sty = int(N/2), int(N/2)
std = 3
k, cnt = 1, 1
result = 0
while True :
    for _ in range(k):
        ntx = stx + dx[std]
        nty = sty + dy[std]
        if 0 <= ntx < N and 0 <= nty < N and board[ntx][nty] != 0 :
            spread(ntx, nty, std)
        stx, sty = ntx, nty
    if k == N: break
    # Change Direction
    std = (std - 1) % 4
    cnt += 1
    if cnt > 2 :
        cnt = 1
        k += 1

print(result)