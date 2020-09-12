# Author: Sarthak Singh sxs6666@psu.print

#grade1 = (input(f"Enter your course 1 letter grade: "))
#credit1 = (input(f"Enter your course 1 credit: "))

def getGradePoint(grade):
  if grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.67    
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0   
  elif grade == "B-":
    return 2.6
  elif grade == "C+":
    return 2.3         
  elif grade == "C":
    return 2.0     
  elif grade == "D":
   return 1.0    
  else:
    return 0.0
        
def run():
  grade_input1 = (input("Enter your course 1 letter grade: "))
  credit_input1 = (input("Enter your course 1 credit: "))  
  print(f"Grade point for course 1 is: {getGradePoint(grade_input1)}")
  grade_input2 = (input("Enter your course 2 letter grade: ")) 
  credit_input2 = (input("Enter your course 2 credit: ")) 
  print(f"Grade point for course 1 is: {getGradePoint(grade_input2)}")
  grade_input3 = (input("Enter your course 3 letter grade: "))  
  credit_input3 = (input("Enter your course 3 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(grade_input3)}")

  GPA = (getGradePoint(grade_input1) * int(credit_input1) + getGradePoint(grade_input2) * int(credit_input2) + getGradePoint(grade_input3) * int(credit_input3)) / (int(credit_input1) + int(credit_input2) +  int(credit_input3))

  print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
  run() 
  
 


#grade2 = (input(f"Enter your course 2 letter grade: "))
#credit2 = (input(f"Enter your course 2 credit: "))










#GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 