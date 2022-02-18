import itertools

def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in perm(s[:i] + s[i+1]):
            res.append(c+cc)
        return res

    def perm2(s):
        res = itertools.permutations(s)
        return ["".join(i) for i in res]

    if __name__ == "__main__":
        val = "012"
        print(perm(val))
        print(perm2(val))


# 순열과 조합 - combinations, permutations
# 이번 강의에서는 iterable의 원소로 순열과 조합을 구하는 방법을 배워봅시다.

# 예시)

# 1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
# 'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 permutation 함수를 구현합니다.

# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result
# 코드를 정정해주신 Jay Kim 님께 감사드립니다.

# 파이썬에서는
# itertools.permutation를 이용하면, for문을 사용하지 않고도 순열을 구할 수 있습니다.

# import itertools

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
# ※ 조합은 itertools.combinations를 사용해서 구할 수 있습니다. 사용법은 permutations와 비슷해요!

# 본 강의는 [Mark Ha]의 아이디어로 제작되었습니다.

# 순열 : https://docs.python.org/3/library/itertools.html#iter-tools.permutations
# 조합 : https://docs.python.org/3/library/itertools.html#iter-tools.combinations