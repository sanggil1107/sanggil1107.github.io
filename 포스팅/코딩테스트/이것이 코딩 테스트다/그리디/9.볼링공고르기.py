# from itertools import combinations

# total = []
# n, m = map(int, input().split())
# item = list(map(int, input().split()))
# result = list(combinations(item, 2))
# print(result)

# for i in range(len(result)):
#     if result[i][0] != result[i][1]:
#         total.append(result[i])

# print(total)
# print(len(total))

n, m = map(int, input().split())
item = list(map(int, input().split()))

count = 0
for i in range(len(item)):
    for j in range(i-1, len(item)):
        if item[i] != item[j]:
            count+=1

print(count)