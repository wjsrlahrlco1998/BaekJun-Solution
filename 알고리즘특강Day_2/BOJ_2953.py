participantScoreList=[]
winerNo=0
winerScore=0

for _ in range(5):
    participantScoreList.append(list(map(int,input().split())))

for i in range(5):
    if sum(participantScoreList[i]) > winerScore:
        winerNo=i+1
        winerScore=sum(participantScoreList[i])

print(f'{winerNo} {winerScore}')