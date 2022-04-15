check = list("CAMBRIDGE")

in_txt=list(input())
result=''

for i in in_txt:
    if i not in check:
        result+=i

print(result)