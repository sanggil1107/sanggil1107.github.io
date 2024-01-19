# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  min_data = min(data)
  result = max(result, min_data)

print(result)