def alternate(n, value1, value2):
    arr = []
    if n != 0:  
        arr = [value1]
    for x in range(n-1):
        if arr[-1] == value1:
            arr.append(value2) 
        elif arr[-1] == value2:
            arr.append(value1)
    return arr
