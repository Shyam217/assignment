
total_students_record = []

class StudentHeight():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def student_object(self):
        obj = {"Name": self.name,
                "Height": self.height,
                "Weight": self.weight}
        return obj
def search_by_name(total_students_record, name):
    for i in total_students_record:
        if name in i["Name"]:
            string = "Name: {}  Height: {}  Weight: {}".format(name, i["Height"], i["Weight"])
            return string
        else:
            print("Name is not existed")
def Avg_height(total_students_record):
    summ = 0

    for j in total_students_record:
        summ += j["Height"]
        avg_height = summ//len(total_students_record)
    return avg_height
def Avg_weight(total_students_record):
    summ = 0

    for k in total_students_record:
        summ += k["Weight"]
        avg_weight = summ//len(total_students_record)
    return avg_weight
def sorting(total_students_record):
    greatest = 0
    new_list = []
    for s in total_students_record:
        if s["Height"] > greatest:
            greatest = s["Height"]
            new_list.append(s)
        else:
            new_list.insert(0, s)
    return new_list



while True:
    user_input = input("Enter\n 1 for Adding student\n 2 for Deleting Student\n 3 for total record\n 4 for Individual record\n 5 for EXIT\n")
    print()
    if user_input == "1":
        name = input("Enter name of the student: ")
        height = int(input("Enter height of the student: "))
        weight  = int(input("Enter weight of the student: "))
        student = StudentHeight(name, height, weight)
        student_obj = student.student_object()
        total_students_record += [student_obj]
        
    elif user_input == "2":
        name = input("Enter name of the Student: ")
        if len(total_students_record) > 0:
            for i in total_students_record:
                if name in i["Name"]:
                    index = total_students_record.index(i)
                    total_students_record.pop(index)
        else:
            print("No records found")
            print()
    elif user_input == "3":
        sorted_list = sorting(total_students_record)
    
        print(sorted_list)
        print()
    elif user_input == "4":
        result = input("1 for individual height\n 2 for Average Height\n 3 for Average Weight")
        print()
        if result == "1":
            name = input("Enter name")
            height = search_by_name(total_students_record, name)
            print(height)
            print()
        elif result == "2":
            avg_height = Avg_height(total_students_record)
            print("Average Height of students: ", avg_height)
            print()
        elif result == "3":
            avg_weight = Avg_weight(total_students_record)
            print("Average weight of students: ", avg_weight)
            print()
    elif user_input == "5":
        break
    else:
        print("Enter valid input")
        print()