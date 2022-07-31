N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def combination(arr, t):
    result = []
    if t == 0 :
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1 : ]
        for C in combination(rest_arr, t - 1):
            result.append([elem] + C)
    return result

coord_list = []

for i in range(1, N - 1):
    for j in range(1, N - 1):
        coord_list.append([i, j])

seed_list = combination(coord_list, 3)

# up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve():
    minValue = 1e9
    for temp in seed_list :
        visited = [[False for _ in range(N)] for _ in range(N)]
        price = 0
        for x, y in temp :
            visited[x][y] = True
            died = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                else :
                    # Died
                    died = True
                    break
            if died :
                break
        # Count Price
        if not died :
            for j in range(N):
                for k in range(N):
                    if visited[j][k] :
                        price += board[j][k]
            minValue = min(minValue, price)
    return minValue

print(solve())