def dont_give_me_five(start,end):
    print(start)
    n = 1
    if start == 4:
        start += 2
        n += 0
        print(start)
    while start < end:          
        if start == 5:
            start += 1  
            print(start)
        else:
            start += 1
            n += 1
            print(start)
    return n
