a = 'ababcdcdababcdcd'

m = 999999

for i in range(1, len(a)):
  temp = a[0:i]
  count = 1
  result = []
  for j in range(1, len(a)):
    print(a[j*i:j*i+i])
    if a[j*i:j*i+i] != '':
      if temp == a[j*i:j*i+i]:
        count+=1
        if j == len(a)-1:
          result+=(str(count) + temp)
      else:
        if count == 1:
          result+=temp
        else:
          result+=(str(count) + temp)
        count=1
      temp = a[j*i:j*i+i]
  print(i, result, len(result))
  
  if m > len(result):
    m = len(result)

print(m)