n = input()
count = 0

if int(n) < 10:
    n = '0' + n
new = n

while True:
    before = str(int(new[0]) + int(new[1]))
    new = new[-1] + before[-1]
    count+=1
    if n == new:
        print(count)
        break