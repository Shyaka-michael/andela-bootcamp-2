def find_missing(num_list_1, num_list_2):
    if len(num_list_1) == 0 and len(num_list_2) == 0:
        return 0
    else:
        num_set_1 = set(num_list_1)
        num_set_2 = set(num_list_2)
        missing_number = list(num_set_1.symmetric_difference(num_set_2))
        print(missing_number)
        if len(missing_number) == 0:
            return 0
        else:
            return missing_number[0]