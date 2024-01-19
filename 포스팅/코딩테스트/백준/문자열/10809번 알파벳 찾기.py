# 나의 답
s = input()

alphabet = [-1] * 26

for i in range(len(s)):
    if alphabet[int(ord(s[i])) - 97] == -1:
        alphabet[int(ord(s[i]))-97] = i

for i in alphabet:
  print(i, end=' ')

# 모범 답
s = input()
alphabet = list(range(97, 123)) # 아스키코드 알파벳 소문자 범위
print(alphabet)
print(chr(97))
for x in alphabet:
    print(s.find(chr(x)), end=" ")
