#https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    half_num = len(nums)/2
    check_num = len(list(set(nums)))
    if half_num >= check_num:
        return check_num
    else:
        return half_num

print(solution([3,3,3,1,1,1,2,2,2,4]))
