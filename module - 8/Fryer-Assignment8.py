import json
import os

def loadJson():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "student.json")
    
    with open(file_path, "r") as file:
        students = json.load(file)
        
    return students

def saveJson(students):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "student.json")
    
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)
     
    print()   
    print("The student json file was updated.")
        
def printJson(students, reasonForPrint):
    print()
    print(reasonForPrint)
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")
    

def main():
   
    # Load the Json into a variable
    students = loadJson()
    
    #print the original list
    printJson(students, "Original Student List:")
    
    # Adding the new student to the end of the student object
    newStudent = {
        "F_Name": "Daniel",
        "L_Name": "Fryer",
        "Student_ID": 123456,
        "Email": "dfryer@my365.bellevue.edu"
    }
    
    students.append(newStudent)
    
    #print with the added student
    printJson(students, "Updated Student List:")
    
    #save the updated list back to the file
    saveJson(students)
    

if __name__ == "__main__":
    main()