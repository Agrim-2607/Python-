final=[]
def EOReplace(L):
    for i in range(len(L)):
        if L[i]%2==0:
            L[i]=L[i]+1
        else:
            L[i]=L[i]-1
    print(L)
L=[10,20,30,40,35,55]
EOReplace(L)
