def solution(prices):
    share = [0] * len(prices)
    for x in range(len(prices)):
        for i in range(x+1, len(prices)):
            share[x] +=1
            if(prices[i] < prices[x]):
                break
    return share