paulList=list(input().split())
paulDict=dict()

for name in paulList:
    if paulDict.get(name):
        paulDict[name] += 1
    else:
        paulDict[name] = 1

minValue = min(list(paulDict.values()))
for name in paulDict:
    if paulDict[name] == minValue:
        print(name)
print(minValue)
