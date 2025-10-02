Arr=list(input("Enter strings"))
l=len(Arr)
t=''
for i in range(0,l-1):
    for j in range(i+1,l):
        if len(Arr[i])>len(Arr[j]):
            t=Arr[i]
            Arr[i]=Arr[j]
            Arr[j]=t
print(Arr)
        
        
    
