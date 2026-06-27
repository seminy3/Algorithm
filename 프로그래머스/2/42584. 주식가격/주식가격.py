def solution(prices): #prices = 초 단위 주식 가격
    share = []
    
    for x in range(len(prices)):    
        t = 0
        for i in range(x+1, len(prices)):
            if(prices[i] >= prices[x]):
                t += 1
            else:
                t += 1
                break
        share.append(t)
    return share