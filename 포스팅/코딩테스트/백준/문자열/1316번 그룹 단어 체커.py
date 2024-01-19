# 나의 답
n = int(input())
count = 0

for _ in range(n):
    st = input()
    a = st[0]
    t = []

    for i in range(1, len(st)):
        if a != st[i]:
            if st[i] in t:
                a = 0
                break
            else:
                t.append(a)
                a = st[i]
    
    if a != 0:
        count+=1

print(count)

# 모범 답
n = int(input())

for _ in range(n):
  st = input()

  for i in range(len(st)-1):
      if st[i] != st[i+1]:
          if st[i] in st[i+1:]:
              n -= 1
              break
  
print(n)