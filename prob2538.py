# 모눈종이의 왼쪽 아래 꼭짓점의 좌표 (0, 0) 오른쪽 위의 꼭짓점 좌표 (N, M)
# x, y 평소와 다르게 역전 / 고로 상하좌우 움직이는 것도 반대로 / 실은 상관없다.

M, N, K = map(int, input().split())
rec_list = [list(map(int, input().split())) for _ in range(K)]

# 격자 안에 사각형 만들어두기
board = [[0 for _ in range(N)] for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 사각형 격자 채우자
def rectangular():
    for rec in rec_list :
        y1, x1, y2, x2 = rec
        x1, x2 = min(x1, x2) - 0.5, max(x1, x2) - 0.5
        y1, y2 = min(y1, y2) - 0.5, max(y1, y2) - 0.5
        for i in range(M):
            for j in range(N):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 1

def solve():
    rectangular()
    size_temp = []
    visited = [[False for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if board[i][j] == 0 and not visited[i][j] :
                q = [[i, j]]
                visited[i][j] = True
                cnt = 1
                while q :
                    x, y = q[0]
                    del q[0]
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] :
                            if board[nx][ny] == 0:
                                visited[nx][ny] = True
                                q.append([nx, ny])
                                cnt += 1
                size_temp.append(cnt)
    print(len(size_temp))
    size_temp.sort()
    print(" ".join(map(str, size_temp)))

solve()
