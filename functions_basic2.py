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


# 6. Minimum
def minimum(arr):
    if len(arr)<1:
        return(False)
    else:
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
    return(min)
print(minimum([]))
print(minimum([5,3,-1,6,-7,10]))


# 7. Maximum
def maximum(arr):
    if len(arr)<1:
        return(False)
    else:
        max = arr[0]
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
    return(max)
print(maximum([]))
print(maximum([5,3,-1,6,-7,10]))


# 8. Ultimate Analysis
def ultimate_anaylysis(arr):
    values = {'sumTotal': 0, 'average' : 0, 'minimum': arr[0], 'maximum': arr[0], 'length': 0}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if arr[i]<values['minimum']:
            values['minimum']= arr[i]
            continue
        if arr[i]>values['maximum']:
            values['maximum']=arr[i]
    values['sumTotal'] = sum
    values['average'] = sum/len(arr)
    values['length'] = len(arr)
    return(values)
print(ultimate_anaylysis([3,7,10,-4,8,1]))


# 9. Reverse List
def reverse_list(arr):
    length = len(arr)
    for i in range(int(length/2)):
        temp = arr[i]
        arr[i] = arr[length-i-1]
        arr[length-i-1] = temp
    return arr
print(reverse_list([1,2,3,4,5,6,7]))
print(reverse_list([1,2,3,4,5,6]))
