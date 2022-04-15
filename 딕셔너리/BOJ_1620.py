poketmonCount, quizCount = map(int, input().split())
poketmonNameDict = {}
poketmonNumDict = {}
answer = []

for i in range(1, poketmonCount + 1):
    poketmonName = input()
    poketmonNameDict[poketmonName] = i
    poketmonNumDict[i] = poketmonName

for _ in range(quizCount):
    quiz = input()
    if '0' <= quiz[0] <= '9':
        answer.append(poketmonNumDict[int(quiz)])
    else:
        answer.append(poketmonNameDict[quiz])

print(*answer, sep='\n')