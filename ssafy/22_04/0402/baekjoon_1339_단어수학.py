from sys import stdin
# 입력 받기
N = int(stdin.readline())
alphabet = [stdin.readline().strip() for _ in range(N)]
# 이 리스트에 각 단어에 몇자리 수가 들어가는지 확인(이 수를 비교하면서 9부터 0까지 입력)
lst = [0] * 26
# 그 알파벳이 어떤 숫자를 부여 받았는지 알려주는 리스트
num = [0] * 26
# 어떤 알파벳이 append되는지 확인하기 위함.
what_alpha = []
# 여기서 어떤 알파벳이 몇자리에 속하는지, 또한 어떤 알파벳이 이안에 있는지 확인
for alpha in alphabet:
    length = len(alpha)
    for i in range(length):
        lst[ord(alpha[i]) - 65] += 10 ** (length - i)
        if ord(alpha[i]) - 65 not in what_alpha:
            what_alpha.append(ord(alpha[i]) - 65)
# 알파벳 내를 돌면서 가장 큰 자리수를 가진 숫자에 가장 큰 9를 주고 차래되로 점점 줄어든다
input_num = 9
while what_alpha:
    max_num, max_idx = 0, 0
    for i in what_alpha:
        # 가장 앞에 있는 두수를 비교 했을 해서 현재수가 더 크면 max_num바꾸기
        if lst[i] > max_num:
            max_num = lst[i]
            max_idx = i
    num[max_idx] = input_num
    input_num -= 1
    what_alpha.remove(max_idx)

total = 0
for alpha in alphabet:
    n = 0
    for a in alpha:
        n = n * 10 + num[ord(a) - 65]
    total += n

print(total)
