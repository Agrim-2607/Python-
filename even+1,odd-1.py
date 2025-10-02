def EOreplace(l):
    for i in range(len(l)):
        if l[i]%2==0:
            l[i]=l[i]+1
        else:
            l[i]=l[i]-1
l=[1,2,3,4,5,6,7,8,9]
EOreplace(l)
print(l)  
