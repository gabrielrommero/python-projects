import statistics

names = input("Full name: ")
score1 = float(input("Score 1st Exam: "))
score2 = float(input("Score 2nd Exam: "))
score3 = float(input("Score 3rd Exam: "))
att = float(input("Attendance Percentage: "))
avarage = statistics.mean([score1,score2,score3])
if score1 >= 0 and score1 <= 100:
    if score2 >= 0 and score2 <= 100:
        if score3 >= 0 and score3 <= 100:
            print("Avarage = ", avarage)
else:
    print("The scores must be on a scale from 0 to 100")

name_list = list(names.split(" "))
initial = ""
for initials in name_list:
    initial = initial + initials[0].upper()
print("Initial: ",initial)


    
print(name_list[1].upper())



grade = avarage
if att < 75:
    print("Grade: F")
elif att >100:
    print("The program cannot run, verify your data")
elif grade >= 85 and grade <= 100:
    print("Grade: A")
elif grade >= 70 and grade < 85:
    print("Grade: B")
elif grade >= 55 and grade < 70:
    print("Grade: C")
elif grade >= 40 and grade < 55:
    print("grade: D")
elif grade < 40:
    print("grade: F")
else:
    print("The program cannot run, verify your data")

gpa = (4*avarage)/100
print("GPA: ", gpa)
