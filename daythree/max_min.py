def find_max_min(num):
    num.sort()

    min_num = num[0]
    max_num = num[-1]

    array_of_min_max = [min_num, max_num]

    if len(num) < 2:
        return False
    elif min_num == max_num:
        array_of_min_max = [min_num]
        return array_of_min_max
    else:
        return array_of_min_max

