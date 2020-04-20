#Enter your code here. Read input from STDIN. Print output to STDOUT

class Student:

    def __init__(self,roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        no_of_sub = 0
        total_marks = 0
        for i in self.marks:
            total_marks = total_marks + i
            no_of_sub = no_of_sub +1
        
        percentage = int(total_marks/no_of_sub)
        return (percentage)
  
    def find_grade(self):
        no_of_sub = 0
        total_marks = 0
        for i in self.marks:
            total_marks = total_marks + i
            no_of_sub = no_of_sub +1
        p = int(total_marks/no_of_sub)

        if (p >= 80):
            return 'A'

        elif (p>=60) and (p<80):
            return 'B'

        elif (p>=40) and (p<60):
            return 'C'

        else:
            return 'F'



if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks)
    print(s.calculate_percentage())
    print(s.find_grade())