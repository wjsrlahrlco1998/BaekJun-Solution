check=['c=','c-','dz=','d-','lj','nj','s=','z=']

s=input()
for i in check:
    s = s.replace(i,'@')

print(len(s))