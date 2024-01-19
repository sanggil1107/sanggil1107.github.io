# 나의 답
s = input()
count = 0
temp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
t = ''

for i in temp:
    while i in s:
        index = s.find(i)
        if index > 0:
            s = s[0:index] + ' ' + s[index+len(i):]
        else:
            s = s[index+len(i):]
        count += 1
s = s.split()
for i in s:
    t += i
count += len(t)
print(count)

# 모범 답
s = input()
al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in al:
  s = s.replace(a, '*')

print(len(s))