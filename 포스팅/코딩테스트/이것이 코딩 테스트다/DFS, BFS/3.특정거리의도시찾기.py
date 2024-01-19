from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# 너비 우선 탐색
queue = deque([x])
while queue:
  v = queue.popleft()
  for g in graph[v]:
    if distance[g] == -1:
      distance[g] = distance[v] + 1
      queue.append(g)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)