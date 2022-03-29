def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        array2 = array[i-1:j]
        array2.sort()
        answer.append(array2[k-1])

    return answer