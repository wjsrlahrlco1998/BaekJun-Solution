# word_a : 가로, word_b : 세로

word_a,word_b=input().split()
l_idx_a=[]
l_idx_b=[]
count=0

for idx_a,c_a in enumerate(word_a):
    for idx_b,c_b in enumerate(word_b):
        if c_a == c_b:
            l_idx_a.append(idx_a)
            l_idx_b.append(idx_b)

for i in range(len(word_b)):
    if i == l_idx_b[0]:
        print(word_a)
    else:
        for j in range(len(word_a)):
            if j == l_idx_a[0]:
                print(f'{word_b[count]}',end='')
            else:
                print('.',end='')
        print()
    count += 1