def solution(progresses, speeds):

    fin_dates = []
    N = len(progresses)
    for i in range(N):
        #  x is finished date such that a + bx <= 100
        a = progresses[i]
        b = speeds[i]
        x = (100- a) // b
        if (100 - a) % b != 0:
            x = x + 1
        fin_dates.append(x)

    answer = []
    cur_max = fin_dates[0]
    cur_cnt = 1
    del fin_dates[0]

    for val in fin_dates:
        if cur_max >= val:
            cur_cnt = cur_cnt + 1
        else: 
            answer.append(cur_cnt)
            cur_max = val
            cur_cnt = 1

    answer.append(cur_cnt)
    return answer