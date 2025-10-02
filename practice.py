#mylist=[1,2,3,4,5,6,7,8,9,10]
#del mylist[3:]
#print(mylist)


#lst1=[1,2,3]
#lst2=[4,5,6]
#lst1+=lst2
#print(lst1)

#obj1=(10,15,25,30)
#obj1[2]=20
#print(obj1)

#strg=''SRGS''
#print(strg)

#t1=(1,2,4,3)
#t2=(1,2,3,4)
#print(t1<t2)

#def func(a,b=5, c=10):
#    print('a is',a, 'and b is', b, 'and c is', c)
#func(3,7)
#func(25, c=24)
#func(c=50, a=100)

#fruit={}
#L=['Orange', 'Apple', 'Grapes']
#for index in L:
#    if index in fruit:
#        fruit[index]+=1
#    else:
#        fruit[index]=1
#        print(len(fruit))
#        print(fruit)

#for i in range(3,10,2):
#    print(i*'$')

#print("acccccccddddd".find("d", 0, 9))
'''
k=1
for i in range(1,5):
    for j in range(0,i):
        if i==1:
            print(k, end='')
        if i==2:
            print(k,k+2, end='')
        if i==3:
            print(k,k+2,k+4, end='')
        if i==4:
            print(k,k+2,k+4,k+6, end='')        
    print()    
'''

'''
y=str(123)
x="hello"*3
print(x,y)
x="hello"+"world"
y=len(x)
print(x,y)
'''

'''
x="hello"+\
   "to python"+\
   "world"
for char in x:
    y=char
    print(y,':',end="")

x="hello world"
print(x[:2],x[:-2],x[-2:])
print(x[6],x[2:4])
print(x[2:-3],x[-4:-2])
'''

'''
i=1
for i in range(5):
    while True:
        print(i)
'''

'''
for i in range(-5,-7,-1):
    print(i+1)

s="PYTHON PROGRAMMING"
#print(s[-15:-16])
print(s[-15:-16:-1])
'''

'''
Name="PythoN3@1"
R=" "
for x in range(len(Name)):
    if Name[x].isupper():
        R=R+Name[x].lower()
    elif Name[x].islower():
        R=R+Name[x].upper()
    elif Name[x].isdigit():
        R=R+Name[x-1]
    else:
        R=R+"#"
        print(R)
'''

'''
def func(num1,num2):
    result=num1+num2
    print("Aditiion=", result)
a=int(input("Enter first number:"))    
b=int(input("Enter sec number:"))
func(a,b)
'''

'''
def ListChange():
    for i in range(len(L)):
        if L[i]%2==0:
            L[i]=L[i]*2
        elif L[i]%3==0:
            L[i]=L[i]*3
        else:
            L[i]=L[i]*5 
L=[2,6,9,10]
ListChange()
for i in L:
    print(i, end='#')
'''
'''
v=25
def Fun(ch):
    v=50
    print(v, end=ch)
    v*=2
    print(v, end=ch)
print(v, end='*')
Fun('!')
print(v)
'''

'''
a=[4,5,6,7]
try:
    print("First element is %d" %(a[0]))
    print("Lat elemt is %d" %(a[4]))
except:
    print("Error")
'''

'''
LS=["HIMALAYA","NILGIRI","ALASKA","ALPS"]
D={}
for S in LS:
    if len(S)%4==0:
        D[S]=len(S)
        print(D[S])
for K in D:
    print(K,D[K],sep='#')
'''
'''
students={"ANITA":90,"NISHA":76,"ASHA":92}
students.pop("NISHA")
print(students)
'''
'''
message="This is his book"
count=message.count("is")
print(count)        
'''
'''
mystr="MISSISSIPPI"
print(mystr[:4]+"#"+mystr[-5:])
'''
'''
event="G20 Presidency@2023"
L=event.split(' ')
print(L[::-2])
'''
'''
a=20
def convert(a):
    b=20
    a=a+b
    return a
print(convert(10))
print(a)
'''
'''
def callon(b=20,a=10):
    b=b+a
    a=b-a
    print(b,"#",a)
    return b
x=100
y=200
x=callon(x,y)
print(x,"@",y)
y=callon(y)
print(x,"@",y)
'''
'''
S="Racecar Car Radar"
L=S.split()
for W in L:
    x=W.upper()
    if x==x[::-1]:
        for I in x:
            print(I, end="*")
    else:
        for I in W:
            print(I, end="#")
    print()
'''
'''
D={'S01':95, 'S02':96}
for I in D:
    print(I, end='#')
'''
'''
def change(N):
    N=N+10
    print(N,end='$$')
N=15
change(N)
print(N)
'''

# s=0
# for i in range(10):
#    s=+1
#    print(s)

# import math
# help(pow)
















