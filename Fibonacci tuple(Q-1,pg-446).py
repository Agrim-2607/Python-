a=0
b=1
s=0
L=[0,1]
for i in range(0,8):
    s=a+b
    L=L+[s]
    a=b
    b=s
T=tuple(L)
print(T)
