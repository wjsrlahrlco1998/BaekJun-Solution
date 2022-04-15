n=int(input())
l=[]
l2=[]
for _ in range(n):
    idx,s=input().split()
    l.append(int(idx))
    l2.append(s)

for i in range(n):
    l2[i]=l2[i][:l[i]-1]+l2[i][l[i]:]
    print(l2[i])