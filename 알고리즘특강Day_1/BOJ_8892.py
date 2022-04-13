#

# 테스트 케이스의 수
t=int(input())

for _ in range(t):
    n = int(input())
    l = []
    flag = 0
    # 단어 저장
    for _ in range(n):
        l.append(input())
    # 단어 합친 후 비교
    for i in range(n):
        for j in range(n):
            if i != j:
                s=l[i]+l[j]
                r_s = s[::-1]
                if s==r_s:
                    print(s)
                    flag=1
                    break
        if flag == 1:
            break
    if flag == 0:
        print(0)

