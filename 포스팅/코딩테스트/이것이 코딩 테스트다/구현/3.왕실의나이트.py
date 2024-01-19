input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0
steps = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]


for step in steps:
    x = row + step[0]
    y = column + step[1]
    if x <= 8 and x >=1 and y <= 8 and y >= 1:
        count+=1

# for i in range(len(steps)):
#     x = row + steps[i][0]
#     y = column + steps[i][1]
#     if x <= 8 and x >=1 and y <= 8 and y >= 1:
#         count+=1

print(count)