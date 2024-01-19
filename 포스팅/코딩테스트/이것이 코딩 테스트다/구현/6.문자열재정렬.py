n = input()
word = []
number = 0

for i in n:
  if i.isdigit():
    number+=int(i)
  else:
    word.append(i)


word.sort()

if number != 0:
  word.append(str(number))

for i in range(len(word)):
  print(word[i], end='')
