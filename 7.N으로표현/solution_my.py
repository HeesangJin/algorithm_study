def solution(N, number):
    answer = 0
    max_count_number = 8
    nums_using_times = [[-1]] # 0 times

    for i in range(1, max_count_number+1):
        # case 1. repeats N i times.
        number_repeated_N_i_times = int("".join(str(N)*i))
        nums_using_times.append([number_repeated_N_i_times])

        # case 2~5. nums_using_times[i-1] <op> nums_using_times[i-1] for { +, -, *, / } each.
        for j in range(1, i):
            nums_result = numbers_with_op(nums_using_times[j], nums_using_times[i-j])
            nums_using_times[i].extend(nums_result)

        nums_using_times[i] = list(dict.fromkeys(nums_using_times[i]))
        if(nums_using_times[i].count(number) > 0):
            return i

    print(nums_using_times)
    return -1

def numbers_with_op(nums1,  nums2):
    nums_result = []
    for num1 in nums1:
        for num2 in nums2:
            nums_result.append(num1+num2)
            nums_result.append(num1-num2)
            nums_result.append(num1*num2)
            if num2 != 0:
                nums_result.append(int(num1/num2))
    return nums_result