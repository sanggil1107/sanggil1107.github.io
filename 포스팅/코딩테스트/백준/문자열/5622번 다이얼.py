# 나의 답
dial = [
  [],
  [],
  ['A', 'B', 'C'],
  ['D', 'E', 'F'],
  ['G', 'H', 'I'],
  ['J', 'K', 'L'],
  ['M', 'N', 'O'],
  ['P', 'Q', 'R', 'S'],
  ['T', 'U', 'V'],
  ['W', 'X', 'Y', 'Z']
]

result = 0
st = input()

for s in st:
  for i in range(len(dial)):
    for d in dial[i]:
      if s == d:
        result += i + 1


print(result)

# 모범 답
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

st = input()

result = 0

for s in st:
  for d in dial:
    if s in d:
      result += dial.index(d) + 3

print(result)