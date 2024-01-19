n = int(input())

array = []

for i in range(n):
  data = input().split()
  array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
  print(student[0], end=' ')

print(array)