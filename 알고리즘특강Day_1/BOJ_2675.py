#26~30

n=int(input())

for _ in range(n):
    result=''
    num, s = input().split()
    for j in s:
        print(j*int(num),end='')
    print()
