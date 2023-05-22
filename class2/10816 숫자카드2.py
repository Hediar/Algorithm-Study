import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
index, m_dic = 0, {}
# targets의 원소가 key, 해당 원소가 몇개 있는지 value

for i in sorted(targets):  # sorted(targets)에 해당하는 값만
    cnt = 0
    if i not in m_dic:  # i가 m_dic에 있는지 확인 -> 처음에 등장하는 것만 처리
        while index < len(cards):  # 카드의 길이만큼 수행
            if i == cards[index]:  # 값이 존재하는 경우
                cnt += 1
                index += 1
            elif i > cards[index]:  # 확인하려는 값이 크면, 다음 원소를 확인
                index += 1
            else:
                break
        m_dic[i] = cnt
print(' '.join(str(m_dic[i]) for i in targets))
