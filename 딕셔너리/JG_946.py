numOfInput=int(input())
cDict=dict()

for _ in range(numOfInput):
    country,capital = input().split()
    cDict[country] = capital

print(cDict.get(input(), "Unknown Country"))