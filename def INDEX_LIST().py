def INDEX_LIST(L):
    indexlist=[]
    for i in range(len(L)):
        if L[i]!=0:
            indexlist.extend(L,"index=", i)
    print(indexlist)
L=[12,4,0,11,0,56]    
INDEX_LIST(L)    
