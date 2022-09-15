T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    for x, y in info :
        graph[x].append(y)
        graph[y].append(x)


    def bfs():
        q = [1]
        num = 0
        visited[1] = True
        while q :
            loc = q[0]
            del q[0]
            if visited.count(True) == N : return num
            for x in graph[loc] :
                if not visited[x] :
                    visited[x] = True
                    num += 1
                    q.append(x)
    result.append(bfs())

for number in result :
    print(number)