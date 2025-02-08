# Static methods=A method that belong to a class rather than any object from that class(instance) 
#                usually used for  general utility functions

# Instance methods=Best for operations on instances of the class (object)
# Static methods=best for utility function that do not need access to class data

class Emplyee:

    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position=["Manager","post-Manager","Human-resourses","Team-leader"]
        return position in valid_position


Emplyee1=Emplyee("sankit","Manager")
Emplyee2=Emplyee("vansh","post-Manager")
Emplyee3=Emplyee("shubham","Human-resourses")
Emplyee4=Emplyee("sujal","Team-leader")


print(Emplyee.is_valid_position("H.O.D"))
print(Emplyee.is_valid_position("Manager"))
print(Emplyee1.get_info())
print(Emplyee2.get_info())
print(Emplyee3.get_info())
print(Emplyee4.get_info())