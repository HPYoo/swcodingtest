N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 비가 오는건 0부터!!!! 아예 안잠기는 경우도 있다!
def bfs():
    maxValue = 0
    # Find Max Height :
    maxH = 0
    for arr in board :
        maxH = int(max(maxH, max(arr)))
    for h in range(0, maxH + 1) :
        temp = [[x for x in board[i]] for i in range(N)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if temp[i][j] <= h :
                    temp[i][j] = 0
        cnt = 0
        for i in range(N) :
            for j in range(N) :
                if temp[i][j] != 0 and not visited[i][j] :
                    visited[i][j] = True
                    q = [[i, j]]
                    cnt += 1
                    while q :
                        x, y = q[0]
                        del q[0]
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and temp[nx][ny] != 0 :
                                visited[nx][ny] = True
                                q.append([nx, ny])
        maxValue = max(maxValue, cnt)
    return maxValue
print(bfs())