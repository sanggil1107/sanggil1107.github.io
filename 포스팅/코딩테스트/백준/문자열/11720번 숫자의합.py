# 나의 답
n = int(input())
s = input()
sum = 0
for i in s:
	sum += int(i)
print(sum)

# 모범 답
n = input()
print(sum(map(int, input())))