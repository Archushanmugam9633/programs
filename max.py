str=input()
n=[]
for i in str:
    if i not in n:
        n.append(i)
print(len(n))
