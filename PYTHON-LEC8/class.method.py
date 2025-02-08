# class methods=Allows operations related to the class itself
#               Take (cls) as the first parameter,which represents the class itself.

class student:
     
    count=0
    Total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count+=1
        student.Total_gpa+=gpa

    # instance method
    def get_info(self):
        return f"{self.name}={self.gpa}"
  
    @classmethod
    def get_count(cls):
        return f"Total student:{cls.count}"

    @classmethod
    def get_average_gpa(cls):
       if cls.count == 0:
           return 0
       else:
           return f"Total  average gpa={cls.Total_gpa/cls.count:.2f}"

student1=student("Sanskar",3.9)
student2=student("Radhe",3.9)
student3=student("jaydeep",3.9)
student4=student("gopal",3.9)



print(student.get_count())
print(student.get_average_gpa())