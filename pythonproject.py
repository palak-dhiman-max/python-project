
print(" ------------- WELCOME  TO  MARKSHEET  GENERATOR  TOOL --------------- ")
Name = input("ENTER NAME OF STUDENT :")
roll_no = int(input("ENTER ROLL NUMBER OF STUDENT :"))
name_of_board = input("ENTER NAME OF BOARD OF STUDENT :")
session = input("ENTER THE SESSION:")
class_1=int(input("ENTER CLASS OF STUDENT:"))
marks =[]
subject = []
grace_marks = 0


n= int(input("ENTER THE NUMBER OF SUBJECTS:"))
for i in range(1,n+1)  :
    
    subject_name = input("ENTER NAME OF SUBJECT:")
  
    print(f"MARKS OF {subject_name} : ",end=" ")
    subject_marks = int(input())
    marks.append(subject_marks)
    subject.append(subject_name)

flag =0
# apply grace marks and adjust the marks if necessay
for i in range (n):
    if(marks[i]<=35 and marks[i]>=30):
        grace_marks+=5
        flag = 1
        marks[i]+=5

        
# calculating percentage
total_marks= sum(marks)
max_marks = n*100
percentage = (total_marks/max_marks)*100
print(f"TOTAL MARKS {total_marks}")
print(f"TOTAL MARKS {percentage:2f}%")

# assigning grade 
if(percentage>=90):
    grade = 'A+'
elif(percentage>=80):
    grade = 'A'
elif(percentage>=70):
    grade = 'B'      
elif(percentage>=60):
    grade = 'C'
elif(percentage>=50):
    grade = 'D'
else:
    grade = 'F'

 #display the marksheet

print("\n-------------------------------------------------------")
print("                  MARKSHEET")
print("-------------------------------------------------------")


print(f"MARKSHEET FOR :{Name}  ",end=" ")
print(f"      ROLL NUMBER :{roll_no},  ")
print(f"SESSION-{session}",end=" ")
print(f"                     CLASS -> {class_1}")
print("                                       ")
print(f"BOARD NAME:{name_of_board}")
print("                                           ")
print("                                              ")
print("-----------SUBJECT WISE MARKS OF STUDENT----------------")
print("                                                ")
for i in range(0,n)  :
    print(f"MARKS OF {subject[i]}:{marks[i]}/100 "  ,        end="  "  )
    if(marks[i]>=35):
        print(f"pass in {subject[i]}")
    else:
        print(f"fail in {subject[i]}")
    

    

print("--------------------------------------------------------")
print("    PERCENTAGE , TOTAL MARKS, GRADE OF STUDENT  ")
print("--------------------------------------------------------")
if(flag==1):
    print("        GRACE MARKS AWARDED")
print(f"        TOTAL MARKS :{total_marks}/{max_marks}")
print(f"        PERCENTAGE: {percentage:2f}%")
print(f"        GRADE: {grade}")
     
print("--------------------------------------------------------")
print("                   STATUS OF RESULT   ")
print("--------------------------------------------------------")
if percentage>=35:
    print("\nstatus:PASSED                       *******     ")
else:
    print("\n status FAILED")

print("--------------------------------------------------------")
print("                                                  ")
print("--------------------------------------------------------")