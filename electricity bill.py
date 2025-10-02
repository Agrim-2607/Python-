RL=int(input("Enter the price per unit electricity(Before 7 units):"))
RG=int(input("Enter the price per unit electricity(After 7 units):"))
Pr=int(input("Enter the power rating(in kilowatt)"))
t=int(input("Enter the time the appliance was on(in hours)"))
P=int
U=int (Pr*t)
print("NO.of units:",U)
if U<=7:
    P=U*RL
if U>=7:
    P=U*RG

print("Bill:",P)
