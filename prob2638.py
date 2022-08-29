N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# Find Outer
def outer():
    # 가장자리 조사
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        if 0 < i < N - 1 :
            j_arr = [0, -1]
        else :
            j_arr = [k for k in range(M)]
        for j in j_arr :
            q = [[i, j]]
            visited[i][j] = True
            while q :
                x, y = q[0]
                del q[0]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
                        if board[nx][ny] == 0 :
                            visited[nx][ny] = True
                            q.append([nx, ny])
    return visited

# Find outline of cheese
def cheese(x, y, v):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if v[nx][ny] :
            cnt += 1
    if cnt >= 2 :
        return True
    else :
        return False

# Solve
def solve():
    it = 0
    init_cheese = 0
    info_c = []
    for i in range(N):
        init_cheese += board[i].count(1)
        for j in range(M):
            if board[i][j] == 1 :
                info_c.append([i, j])
    while True :
        temp = []
        visit = outer()
        if init_cheese == 0 :
            break
        for x, y in info_c :
            check = cheese(x, y, visit)
            if check :
                board[x][y] = 0
                init_cheese -= 1
            else :
                temp.append([x, y])
        info_c = temp
        it += 1
    return it

print(solve())