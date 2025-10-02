Arr=eval(input("enter list"))
l=len(Arr)
c=0
for i in range(0,l-1):
    for j in range(1,l):
        if Arr[i]==Arr[j]and i!=j:
            print(Arr[i])
            c+=1
