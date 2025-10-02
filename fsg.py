D1=eval(int(input("enter dictonary1")))
D2=eval(input("enter dictonary2"))
print(len(D1))
for i in range(0,len(D1)):
    D2.setdefault(int(input("key")),int(input("value")))
print(D1,D2)
for i in range(0,len(D1)):
    if D1.pop(i)==D2.pop(i):
        print("contained")

