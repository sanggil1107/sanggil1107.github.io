n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 방문 위치 지정
r = [[0] * m for _ in range(n)]

count = 1
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

r[x][y] = 1
turn = 0

while True:
    # 왼쪽 방향 회전
    d -= 1
    if d < 1:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]  
    if maps[nx][ny] == 0 and r[nx][ny] == 0:
        r[nx][ny] = 1
        x = nx
        y = ny
        turn = 0
        count += 1
    else:
        turn += 1 
    
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if maps[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny

print(count)