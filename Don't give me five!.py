def dont_give_me_five(start,end):
    n = 0
    for x in range(start, end+1):
        if '5' not in str(x):
            n += 1
    return n
