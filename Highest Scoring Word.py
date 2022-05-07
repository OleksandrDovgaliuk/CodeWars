def high(x):
    arr,numArr= x.split(' '),[]
    for val in arr:
        num = 0
        letters = list(val)
        for word in letters:
            num += ord(word) - 96
        numArr.append(num)
    return arr[numArr.index(max(numArr))]
