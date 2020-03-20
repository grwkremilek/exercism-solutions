
def binary_search(list_of_numbers, number):
    l_index, u_index = 0, len(list_of_numbers)-1
    while l_index <= u_index:
        mid_index = (l_index + u_index)//2
        if list_of_numbers[mid_index] == number:
            return mid_index
        elif list_of_numbers[mid_index] < number:
            l_index = mid_index+1
        elif list_of_numbers[mid_index] > number:
            u_index = mid_index-1
    raise ValueError("Number not in the list")
