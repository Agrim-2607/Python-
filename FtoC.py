temp=int(input("Enter the temperature"))
print("Use 0 for (Celcius) and 1
      for (Ferhanite)")
tt=int(input("Enter the type"))

if tt==1:
    a=temp*(9/5)+32
    print(a)

else:
    a= temp-32*(5/9)
    print(a)
