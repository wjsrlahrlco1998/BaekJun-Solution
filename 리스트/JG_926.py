firstList=[]
secondList=[]
for i in range(2):
    if i == 0:
        print('first array')
    else:
        print('second array')
    tmp_l1=list(map(int,input().split()))
    tmp_l2=list(map(int,input().split()))
    if i == 0:
        firstList.append(tmp_l1)
        firstList.append(tmp_l2)
    else:
        secondList.append(tmp_l1)
        secondList.append(tmp_l2)

for i in range(2):
    print(f'{firstList[i][0]*secondList[i][0]} {firstList[i][1]*secondList[i][1]}'
          f' {firstList[i][2]*secondList[i][2]} {firstList[i][3]*secondList[i][3]}')
