def solution(arr):
    x = 1
    list_1 = [arr[0]]
    while x < len(arr):              
        if list_1[-1] != arr[x]:     
            list_1.append(arr[x])
        x += 1                       
    return list_1