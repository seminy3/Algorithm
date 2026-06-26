def solution(arr):
    list_1 = []

    for x in arr:
        if(list_1[-1:] == [x]):
            continue
        list_1.append(x)
    return list_1

if __name__ == '__main__':
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution(arr))