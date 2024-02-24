Scoresheet = {}
def scoresheet():
        for student in range(3):
                student_name = str(input("Enter student name : "))
                student_score = int(input("Enter student score : "))
                Scoresheet[student_name] = student_score
                #sorted_dict= sorted(Scoresheet.values())
                #print(sorted_dict)
                print(Scoresheet)
scoresheet()
