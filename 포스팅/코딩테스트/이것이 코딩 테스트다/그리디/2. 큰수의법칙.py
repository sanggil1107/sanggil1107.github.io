# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력 받은 수 정렬
data.sort() 

first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번쨰로 큰 수

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  
  if m == 0:
    break
  
  result += second
  m -= 1

print(result)