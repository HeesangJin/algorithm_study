
def solution(n, lost, reserve):

    clothes=[1 for i in range(0, n)]
    for l in lost:
        clothes[l-1] -= 1
    for r in reserve:
        clothes[r-1] += 1

    for i in range(0, n):
        if clothes[i] == 0:
            if i != 0 and clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] = clothes[i] + 1
            elif i != n-1 and clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] += 1
    answer = 0       
    for c in clothes:
        if c >= 1:
            answer += 1

    return answer
