# 1. Countdown
def countdown(a):
    for x in range(a, -1, -1):
        print(x)
print(countdown(9))


# 2. Print and Return
def printReturn(a,b):
    print(a)
    return(b)
print(printReturn(6,3))


# 3. First Plus Length
def plusLength(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum + arr[0]
print(plusLength((2,4,6,8,10)))


# 4. Values Greater than Second
def greaterSecond(arr):
    newArr = []
    for i in arr:
        if i > arr[1]:
            newArr.append(i)
    if len(newArr)<2:
        return(False)
    else:
        print(len(newArr))
        return(newArr)
print(greaterSecond((1,3,7,2,9,0,6)))
print(greaterSecond((0,8,4,5,2,1,6)))


# 5. This Length, That Value
def lengthValue(s,v):
    arr = [v]*s
    return(arr)
print(lengthValue(5,8))
print(lengthValue(10,6))







