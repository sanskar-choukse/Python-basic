# class variable=shared among all instances of a class 
#                Defined outside the constructor
#                Allow you to share data among all object created from that class

class student:
    # class-variable
    class_year=2025
    num_student=0

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address 
        # add ho raha ha num of student ka data
        student.num_student+=1


student1=student("Mayank",21,"104 karas dev nager") 
student2=student("abishek",20,"104 dev nager")       
student3=student("Tanu",22,"22/123 djbdcc indore") 

print(student1.name)
print(student1.age)
print(student1.address)

print(student1.class_year)
# or It's a good pracatices that use only class name for class variable
print(student.class_year)  

# total number of student
print(student.num_student)

print(f"My graduating class of {student.class_year} has {student.num_student} student")
print(student1.name)
print(student2.name) 
print(student3.name)