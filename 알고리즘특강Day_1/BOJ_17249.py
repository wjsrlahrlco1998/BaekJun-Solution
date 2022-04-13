tebo = input()
l = list(tebo)
switch = 0
left = 0
right = 0

for i in l:
    if i in ['(',')']:
        switch = 1

    if i == '@' and switch == 0:
        left+=1
    elif i == '@' and switch == 1:
        right+=1

print(left,right)