wordList=[list(input()) for _ in range(5)]
wordCountList=[len(wordList[i]) for i in range(5)]

for i in range(max(wordCountList)):
    for j in range(5):
        try:
            print(wordList[j][i],end='')
        except:
            pass