Gradelist = []
passing = 0 
num = 1 #Numbering
failed = 0

while True:
    Student_Grade = input(f"Student Grade {num}: ")
    if Student_Grade == "done":
        break
    elif not Student_Grade.isnumeric():
        print("Invalid Output, Must be a number")
        continue
    else:
         Student_Grade=int(Student_Grade)
    if  int(Student_Grade) > 39 and int(Student_Grade) < 101:
        Gradelist.append(Student_Grade)
        if int(Student_Grade) >= 75:
           passing +=1
    else:
        failed  +=1
        continue
    num += 1  

if Student_Grade and passing:
     Total = sum(Gradelist)
     Subjects = len(Gradelist)
     Average = round(Total/Subjects, 2)
     PassPercentage = (passing / Subjects) * 100
else:
     Average = 0
     PassPercentage = 0
     

print(f"Average Grade: {Average}")
print(f"Passed Subjects: {passing} ")
print(f"Passing%: {PassPercentage:.2f}")
print(Gradelist)



