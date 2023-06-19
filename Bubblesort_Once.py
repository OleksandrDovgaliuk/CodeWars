def bubblesort_once(lst):
    sorted_lst = lst[:]

    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] > sorted_lst[i + 1]:
            sorted_lst[i], sorted_lst[i + 1] = sorted_lst[i + 1], sorted_lst[i]

    return sorted_lst

