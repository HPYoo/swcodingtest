from collections import deque
t = int(input())

def bfs(x, y, c_arr, f_arr):
    q = deque([[x, y]])
    while q :
        x, y = q.popleft()
        # 계산 하기 전에 n-1 번째 위치에서 축제장소 도달 가능한가?
        if abs(f_arr[0] - x) + abs(f_arr[1] - y) <= 1000:
            print('happy')
            return
        for i in range(len(c_arr)) :
            if not visited[i] :
                nx, ny = c_arr[i]
                dist = abs(nx - x) + abs(ny - y)
                if dist <= 1000 :
                    q.append([nx, ny])
                    visited[i] = True
    print('sad')
    return

for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    cvs_list = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    bfs(x, y, cvs_list, fest)