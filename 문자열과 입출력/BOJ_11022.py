t = int(input())
l = []
l1 = []
l2 = []
for i in range(t):
    a,b = map(int, input().split())
    l1.append(a)
    l2.append(b)
    l.append(a+b)

for i in range(len(l)):
    print(f"Case #{i+1}: {l1[i]} + {l2[i]} = {l[i]}")