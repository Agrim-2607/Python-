def search_replace():
    for i in range(len(L)):
        if L[i]==NS:
            L[i]=0
    print(L)    
    ch=input("Do you want to search any other number and replace it with 0?(y/n)")
    if ch=="y":
        N=int(input("Enter the number to be searched:"))
        for i in L:
            if L[i]==N:
                L[i]=0
            else:
                print("input number not in L")
L=[10,20,30,10,40]
NS=10
search_replace()
print(L)
