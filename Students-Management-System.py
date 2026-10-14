import time 
import os
class Student:
    num_of_student = 0
    def __init__(self, name, age, number, courses="None"):
        self.__name = name
        self.__age = age
        self.__number = number
        self.__grades = []
        self.__courses = courses 
        Student.num_of_student+=1
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_number(self):
        return self.__number
    def get_grades(self):
        return self.__grades
    def get_courses(self):
        return self.__courses
    def set_grades(self, grades):
        self.__grades.append(int(grades))
    def calculate_average(self):
        if self.__grades:
            return round(sum(self.__grades) / len(self.__grades), 2) 
        else:
            return 0       
    
            
    def display(self):
        return f"""
NAME   : {self.__name}
AGE    : {self.__age}
NUMBER : {self.__number}
GRADES : {self.__grades}
COURSES: {self.__courses}
{("-"*40)}"""
    


all_students = []
def clear():
    os.system("cls")                   
def add_student():
    name = input("name:")
    age = input("age:")
    number = input("number:")
    
    courses = input("courses:")
    return Student(name= name, age= age, number= number, courses= courses)

def display_all_students() :
    if all_students:
        print(f"NUMBER OF STUDENTS AVAILABE: {Student.num_of_student}")
        for student in all_students:
            print(student.display())
            
    else:
        print("No student here now... try to add one!!:)")
def search_for_student():
   found_student = search()
   if not isinstance(found_student, str):
       clear()
       print(found_student.display())
   else :
       print(found_student)
    
def remove_student():
    if all_students:
        student_to_remove = input("Enter number of student that you want to remove:")
        found = False
        for index, student in enumerate(all_students):
            if student.get_number() == student_to_remove:
                all_students.pop(index)
                found = True
                Student.num_of_student -= 1
                print("Removing...")
                break
        if not found:
            print("Student not found")
            
    else:
        print("No student to remove :(")
    
    
def add_grades():
    if all_students:
        found =False
        student_to_add_grades= input("enter student's number to add his grades:")
        for student in all_students:
            if student.get_number() == student_to_add_grades:
                added_grades = (input("Enter student's grades separed by comma (,):")).split(", ")
                for grade in added_grades:
                    
                    student.set_grades(grade)
                print("Adding grades ...")
                found = True
        if not found :
            print("Student not found !")
    else:
        print("No student to add grades :(")
        
def search():
    if all_students:
        avialabe_way = ["Name", "Age", "Number"]
        for index, element in enumerate(avialabe_way):
            print(f"{index+1}.{element}")
        chosed_way = int(input(f"Enter you action :"))
        if isinstance(chosed_way, str):
            return "Invalid input"
        if chosed_way > len(avialabe_way):
            return "invalid input"
        student_info = input(f"Enter student's {avialabe_way[chosed_way-1]} : ")
        
        found = False 
       
        for student in all_students:
                if student.get_name() == student_info or student.get_age() == student_info or student.get_number() == student_info:
                    found = True
                    return student
        if not found:
            return "Student not found"
        
    else:
        return "There is no student right now"   
                
    
    
def set_up():
    print("============================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("============================") 
    
    print("""
1.Add student
2.Display all students
3.Search for student
4.Remove student
5.Add grades
6.Calculate avrege""")
    return input("Choose an action:")                   
while True:
    clear()
    action = set_up()
    
    if action == "1":
        clear()
        all_students.append(add_student())
    
    elif action == "2":
        clear()
        display_all_students()
        time.sleep(10)
        
    elif action == "3":
        clear()
        search_for_student()
        time.sleep(10)
        
    elif action == "4":
        clear()
        remove_student()
        time.sleep(5)
        
    elif action == "5":
        clear()
        add_grades()
        time.sleep(5)
    elif action == "6":
        clear()
        passed_students = 0
        rejected_students = 0
        for student in all_students:
            result = student.calculate_average()
            if result > 44 :
                passed_students += 1
                print(f"NAME : {student.get_name()}")
                print(f"RESULT: {result} >>> Passed :)")
                print("-"*30)
            else:
                rejected_students += 1
                print(f"NAME : {student.get_name()}")
                print(f"RESULT:{result} >>> Rejected :(")
                print("-"*30)
        print(f"PASSED STUDENTS  : {passed_students}")
        print(f"REJECTED STUDENTS: {rejected_students}")
        time.sleep(10)
                
        

        
       
    
            
        
        
        
    
 



    
        
       
    
    
        
    
        
    
        
        
        

