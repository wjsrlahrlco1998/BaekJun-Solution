n, m = map(int, input().split())

nameDict = dict()
nameList = []

for _ in range(n):
    name = input()
    nameDict[name] = 0
for _ in range(m):
    name = input()
    if nameDict.get(name) != None:
        nameDict[name] += 1
    else:
        nameDict[name] = 0

for name, value in nameDict.items():
    if value == 1:
        nameList.append(name)

print(len(nameList))
print(*sorted(nameList), sep='\n')