c = int(input())

for _ in range(c):
    student = list(map(int, input().split()))
    sum = 0
    count = 0
    for i in range(1, student[0]+1):
        sum += student[i]
    avg = sum / student[0]

    # student.sort()
    # mid = len(st)
    # 0번째 원소 빼고 정렬하는 법

    for i in range(1, student[0]+1):
        if student[i] > avg:
            count+=1
    final = count / student[0] * 100
    print(f'{final: .3f}%')