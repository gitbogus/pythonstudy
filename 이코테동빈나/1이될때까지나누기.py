# 1이 될때 까지 : 문제조건
# 첫째 줄에 N(1 <= N<=100,000)과 K(2<=K<=100,000)가 공백을 기준으로 하여 각각 자연수로 주어집니다.
# 첫째 줄에 N이 1이될때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다
# 입력 예시 25 5
# 출력 예시 2

# m = list(map(int, input("두개의 정수를 입력하세요 : ").split()))


n , k = map(int, input("두개의 정수를 입력하세요 : ").split())

result = 0

while True:
    # N이 k로 나누어 떨어지는 수가 될 떄 까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을때 (더이상 나눌수 없을때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

