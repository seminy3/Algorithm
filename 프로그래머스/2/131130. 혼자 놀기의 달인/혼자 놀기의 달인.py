import random


def solution(cards):
    n = len(cards)
    visited = [False] * n      # 각 상자를 열었는지 표시
    cycle_lengths = []         # 각 그룹(사이클)의 길이 저장

    for i in range(n):
        if visited[i]:         # 이미 다른 그룹에 속한 상자면 건너뜀
            continue

        length = 0
        cur = i
        while not visited[cur]:        # 아직 안 연 상자인 동안 반복
            visited[cur] = True        # 이 상자를 '열었음'으로 표시
            length += 1                # 그룹 크기 +1
            cur = cards[cur] - 1       # 카드값(1~n) → 인덱스(0~n-1) 변환 후 이동

        cycle_lengths.append(length)   # 완성된 그룹의 길이 기록

    if len(cycle_lengths) < 2:         # 그룹이 1개뿐 → 2번 그룹 없음
        return 0

    cycle_lengths.sort(reverse=True)   # 길이 내림차순 정렬
    return cycle_lengths[0] * cycle_lengths[1]   # 가장 큰 두 그룹의 곱


if __name__ == "__main__":
    n = int(input("\n카드 수를 입력하세요(2~100): "))
    cards = list(range(1, n + 1))   # 1~n 카드
    random.shuffle(cards)           # 무작위로 섞어 상자에 넣음
    print("섞인 상자:", cards)
    print("최고 점수:", solution(cards))