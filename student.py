class Student:
    def __init__(self,name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade
    def display_info(self):
        print(f"Student Name: {self.name} Student's id: {self.id} Student's grade: {self.grade}")
student1= Student("Mariam",250000, 85)
