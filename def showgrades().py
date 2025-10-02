def showgrades(S):
    for keys,values in S.items():
        if (sum(values))//3>=90:
            Grade="A"
        elif (sum(values))//3<90 and (sum(values))//3>=60:
            Grade="B"
        elif (sum(values))//3<60:
            Grade="C"
        print(keys,'-',Grade)    
S={"AMIT":[92,86,64],"NAGA":[65,42,43],"DAVID":[92,90,88]}
showgrades(S)

