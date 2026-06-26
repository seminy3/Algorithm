def solution(arr):
    x = 1
    i = 1
    list_1 = [arr[0]]
    while True:
        if (x >= len(arr)):
            break
        elif (list_1[i-1] != arr[x]):
            list_1.append(arr[x])
            x += 1
            i += 1
        elif (list_1[i-1] == arr[x]):
            x += 1
            
    answer = list_1
    return answer