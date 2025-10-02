def Searchout(Teachers, Tname):
    for i in range(len(Teachers)):
        if Teachers[i]=="Rahul" or Teachers[i]=="rahul":
            print(Teachers[i],"at",i)
Teachers=["Ankit","Siddhart","Rahul","Sangeeta","rahul"]    
TName="Rahul"
Searchout(Teachers, TName)    
