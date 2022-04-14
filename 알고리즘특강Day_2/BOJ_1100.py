chess=[]
isWhiteCount=0
for _ in range(8):
    chess.append(list(input()))

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    isWhiteCount+=1
    else:
        for j in range(8):
            if j % 2 == 1:
                if chess[i][j] == 'F':
                    isWhiteCount+=1
print(isWhiteCount)