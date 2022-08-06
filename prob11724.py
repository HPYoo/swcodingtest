N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
count = 0
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 낮은 순서대로 정렬해주자
for i in range(1, N+1):
    graph[i].sort()

def bfs(arr):
    global count
    # 너비 탐색이 끝난 뭉치 +1
    visited = [False for _ in range(N + 1)]
    for i in range(1, len(arr)):
        if not visited[i] :
            visited[i] = True
            count += 1
            q = [arr[i]]
            while q :
                x = q[0]
                del q[0]
                for j in x :
                    if not visited[j] :
                        visited[j] = True
                        q.append(arr[j])
    return
bfs(graph)
print(count)
