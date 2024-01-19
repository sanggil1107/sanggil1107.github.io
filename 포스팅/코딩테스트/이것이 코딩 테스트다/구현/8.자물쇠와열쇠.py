
def rotate_90(before):
  #before = [[0,0,0],[1,0,0],[0,1,1]]
  n = len(before)
  after = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      after[j][n-1-i] = before[i][j]

  return after

def check(new_lock, n):
  for i in range(n):
    for j in range(n):
      if new_lock[i+n-1][j+n-1] != 1:
        return False

  return True

def solution(key, lock):
    answer = True
    n = len(lock)
    m = n * 3 - 2
    new_lock = [[0] * m for _ in range(m)]

    for i in range(n):
      for j in range(n):
        new_lock[i+n-1][j+n-1] = lock[i][j]

    for x in range(m-n+1):
      for y in range(m-n+1):
        for i in range(4):
          for j in range(n):
            for k in range(n):
              new_lock[j+x][k+y] += key[j][k] 

          if check(new_lock, n) == True:
            return answer
          else:
            for j in range(n):
              for k in range(n):
                new_lock[j+x][k+y] -= key[j][k] 
            key = rotate_90(key)

    answer = False

    return answer

# key = [[0,0,0],[1,0,0],[0,1,1]]
# lock = [[1,1,1],[1,1,0],[1,0,1]]
# t = solution(key, lock)
# print(t)