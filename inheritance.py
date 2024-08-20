#single inheritance
#multiple inheritance
#multilevel inheritance
#init innitializes automatically once an objecrt is created
class StudentDetail(College):
    def detail(self):
        #super keyword le details of parent class thaanumilxa
        super().show()
        print("Another child class")
detail = StudentDetail('binod', 16,'Xavier')
print(detail.detail())
#hieriarchial inheritance
