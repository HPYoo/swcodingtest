from collections import deque
N = int(input())
step = list(map(int, input().split()))

def bfs():
    minValue = 101
    if len(step) == 1 :
        return 0
    q = deque()
    q.append([1, step[0], 0])
    visited = [False for _ in range(N+1)]
    visited[1] = True
    while q :
        loc_x, x, cnt = q.popleft()
        sign = False
        for i in range(1, x + 1):
            loc_nx = loc_x + i
            if loc_nx < N and not visited[loc_nx]:
                visited[loc_nx] = True
                q.append([loc_nx, step[loc_nx-1], cnt + 1])
            elif loc_nx == N :
                minValue = cnt + 1
                sign = True
                break
        else :
            continue
        if sign :
            break
    return minValue

result = bfs()

if result == 101 :
    print(-1)
else :
    print(result)
