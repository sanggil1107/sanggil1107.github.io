# 나의 답
alphabet = [0] * 26
s = input()
s = s.upper()

for i in s:
    alphabet[ord(i)-65] += 1

m = max(alphabet)
result = list(filter(lambda e:alphabet[e] == m, range(len(alphabet))))

if len(result) > 1:
    print('?')
else:
    print(chr(result[0] + 65))


# 모범 답
word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

# print(word_list, cnt)

if cnt.count(max(cnt)) >= 2:
  print("?")
else:
  print(word_list[cnt.index(max(cnt))].upper())