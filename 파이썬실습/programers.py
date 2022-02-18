def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    return list(d.keys()).pop()

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))