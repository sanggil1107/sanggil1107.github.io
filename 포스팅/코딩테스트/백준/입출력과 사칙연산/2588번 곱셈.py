a = input()
b = input()
temp = 0
x = 1
sum = 0

for i in range(len(b)-1, -1, -1):
  temp = int(b[i]) * int(a)
  print(temp)
  temp *= x
  sum += temp
  x *= 10

print(sum)