class student:
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name

    def nameid(self):
        return self.student_id+" "+self.student_name

std1 = student("27","ava")
details=std1.nameid()
print(details)

setattr(std1,"student_class","10")
b=getattr(std1,"student_class")

delattr(std1,"student_name")
print(hasattr(std1,"student_name"))

setattr(std1,"student_name","prat")
print(getattr(std1,"student_name"))
setattr(std1,"__studentdept","PB")
print(hasattr(std1,"__studentdept"))