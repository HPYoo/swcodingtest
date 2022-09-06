N, M = map(int, input().split())
w_info = [list(map(int, input().split())) for _ in range(M)]

# Wall의 경우의 수 총 16개
w_dict = {}
for i in range(16):
    num = i
    temp_direction = [0, 0, 0, 0]
    it = 0
    while num > 0 :
        remain = num % 2
        temp_direction[it] = remain
        num //= 2
        it += 1
    w_dict[i] = temp_direction

# 서, 북, 동, 남 : 1, 2, 4, 8
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방 구조 파악
def bfs():
    visited = [[False for _ in range(N)] for _ in range(M)]
    cnt = 0
    size = 0
    temp = []
    regime = [[0 for _ in range(N)] for _ in range(M)]
    idx = 1
    for i in range(M):
        for j in range(N):
            q = [[i, j]]
            if not visited[i][j] :
                visited[i][j] = True
                cnt += 1
                size = 1
                while q :
                    x, y = q[0]
                    regime[x][y] = idx
                    del q[0]
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        direction = d
                        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] :
                            # Wall? 내가 향하고자 하는 방향에 벽이 있는지 확인하고 움직이자
                            # 벽 방향 동쪽 = 내 방향 서쪽 / 벽 방향 북쪽 = 내 방향 남쪽
                            wall = w_info[nx][ny]
                            if w_dict[wall][(direction + 2) % 4] != 1 :
                                visited[nx][ny] = True
                                size += 1
                                regime[nx][ny] = idx
                                q.append([nx, ny])
                temp.append(size)
                idx += 1
            else :
                continue
    adj = []
    for i in range(M): # 행 기준
        # 붙어 있는 방 정보 확인
        num_of_room = regime[i][0]
        for j in range(1, N):
            if num_of_room != regime[i][j] :
                if [num_of_room, regime[i][j]]  not in adj and [regime[i][j], num_of_room] not in adj:
                    adj.append([num_of_room, regime[i][j]])
                num_of_room = regime[i][j]
    for j in range(N):
        num_of_room = regime[0][j]
        for i in range(1, M):
            if num_of_room != regime[i][j] :
                if [num_of_room, regime[i][j]] not in adj and [regime[i][j], num_of_room] not in adj:
                    adj.append([num_of_room, regime[i][j]])
                num_of_room = regime[i][j]
    maxValue = 0
    for i, j in adj :
        size = temp[i-1] + temp[j-1]
        maxValue = max(maxValue, size)
    return cnt, max(temp), maxValue

result = bfs()
for i in range(len(result)):
    print(result[i])
