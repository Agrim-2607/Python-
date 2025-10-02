class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum = 0 
        for i in self.marks:
            sum+=i
        print("Your avg score is: ", sum/3)  

    def percentage(self):
        sum = 0 
        for i in self.marks:
            sum+=i
        print("Your percentage is: ", (sum/300)*100)    

            
st1 = Student("Agrim", [99,100,94])
print(st1.name,":-", st1.marks)
st1.avg()
st1.percentage()

print("BINGOOOOO, IN THIS SITUATION YOUR AVG AND % IS SAME!!!")



