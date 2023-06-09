def solution(arr, delete_list):
    answer = []
    for num,i in enumerate(delete_list):
        if i in arr:
            del_index = arr.index(i)
            del arr[del_index]
    answer = arr
    return answer