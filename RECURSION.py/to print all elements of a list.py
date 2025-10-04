def list(L,I=0):
    if I==len(L):
        return
    
    print(L[I], end=" ") 
    list(L,I+1)

fruits=["mango","litchi","banana"]
list(fruits)