def solution(n):
    x = 0
    while True:
        x += 1
        answer = (7*x) / n
        if(answer >= 1):
            break
    return x