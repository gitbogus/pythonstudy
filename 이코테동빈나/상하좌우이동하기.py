# 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다 (1 <=N <= 100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1 <= 이동횟수 <=100)

# 출력조건 : 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분하여 출력합니다.

# 입력 예시 
# 5
# R R R U D D

# 출력 예시
# 3 4

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R , U, D에 따른 이동 방향.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]q2w1
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)