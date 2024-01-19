def prime(p):
    if p == 1:
        return False
    for i in range(2, p-1):
        if p % i == 0:
            return False
    return True # 소수

n = int(input())
datas = list(map(int, input().split()))
count = 0

for data in datas:
  if prime(data):
    count+=1

print(count)