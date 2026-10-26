class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def introduce(self):
        print(f"hi, mai {self.name} hu, {self.course} kar raha hu")

    def show_result(self):
        print(f"Mere marks: {self.marks}")
        if self.marks >= 60:
            print("Result: PASS - Badhai ho!")
        else:
            print("Result: FAIL - Aur mehnat karni hai")

# Ab test karte hain
s1 = Student("Ayush", "BCA AI and Data science", 75)
s1.introduce()
s1.show_result()
print("\nproject start hogya!")