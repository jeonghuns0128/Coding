def solution(arr):
    answer = [[]]
    if len(arr) == len(arr[0]):
        answer = arr
    elif len(arr) < len(arr[0]):
        num = len(arr[0]) - len(arr)
        a_list = []
        for a in range(len(arr[0])):
            a_list.append(0)    
        for i in range(num):
            arr.append(a_list)    
#            arr.append([0,0,0,0])
        answer = arr
    elif len(arr) > len(arr[0]):
        num = len(arr) - len(arr[0])
        for arr2 in arr:
            for i in range(num):
                arr2.append(0)
        answer = arr
    else:
        pass
    return answer