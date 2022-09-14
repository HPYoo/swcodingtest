R, C = map(int, input().split())
hand = int(input())
hand_info = [list(map(int, input().split())) for _ in range(hand)]
sx, sy = map(int, input().split())
# 1 : 위, 2: 아래, 3: 왼쪽, 4 : 오른쪽
d_info = list(map(int, input().split()))
# 없음, 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# Board
board = [[0 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(hand):
    x, y = hand_info[i]
    board[x][y] = -1

def solve():
    q = [[sx, sy]]
    visited[sx][sy] = True
    it = 0
    while True :
        # 지정한 방향으로 한 칸 갔을 때 갈 수 있냐?
        direction = d_info[it]
        while q :
            x, y = q[0]
            del q[0]
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] :
                if board[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append([nx, ny])
        cnt = 0
        q = [[x, y]]
        for d in d_info :
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= R or ny < 0 or ny >= C : cnt +=1
            elif visited[nx][ny] : cnt += 1
            elif board[nx][ny] != 0 : cnt += 1
        if cnt == 4 : break
        it += 1
        if it >= 4 : it = 0
    return [x, y]

result = solve()
print(" ".join(map(str, result)))