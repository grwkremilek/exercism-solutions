SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1, 2, 3, 4

def check_lists(first_list, second_list):
    form_list1 = [' {0} '.format(i) for i in first_list]
    form_list2 = [' {0} '.format(i) for i in second_list]
    string_1 = ''.join(form_list1)
    string_2 = ''.join(form_list2)
    if string_1 == string_2:
        return EQUAL
    elif string_1 in string_2:
        return SUBLIST
    elif string_2 in string_1:
        return SUPERLIST
    return UNEQUAL
