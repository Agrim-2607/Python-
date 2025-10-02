def Puzzle(W,N):
    C=1
    S=' '
    for i in W:
        if C%N==0:
            S=S+'_'
        else:
            S=S+i
        C+=1
    return S
W=input("Enter any word: ")
N=int(input("Enter any number for which every Nth alphabet get replaced by '_': "))
print(Puzzle(W,N))
