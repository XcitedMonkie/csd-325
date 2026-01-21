# Daniel Fryer
# 12/7/2025
# Assignment 9.2

class Student:
    # Initialize the student object with the first and last name
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.totalQualityPoints = 0.0
        self.credits = 0.0 

    # Return the full name of the student
    def getFullName(self):
        return f"{self.firstName} {self.lastName}"   

    # setup the grade scale and the points for each grade
    def GradeScale(self, grade):
        gradeScale = {
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "C-": 1.7,
            "D+": 1.3,
            "D": 1.0,
            "F": 0.0}
        return(gradeScale.get(grade.upper(), 0.0))

    # Calculate the GPA or return 0 if no credits are entered
    def calculateGPA(self):
        if self.credits == 0:
            return 0.0
        return self.totalQualityPoints / self.credits 

def Main():
    validateGradeScale = {"A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"}
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ") 
    lastName = thislastname
    student = Student(firstName, lastName)  

    # Loop to get course information
    while True:
        courseGrade = input("Enter course grade (or 'done' to finish): ").strip()       

        if courseGrade.upper() == "DONE":
            break       

        # check if the entered course grade is a valid grade
        if(courseGrade in validateGradeScale):
            courseCredits = input("Enter course credits: ").strip() 

            try:
                credits = float(courseCredits)
                # check to make sure credits are a positive number
                if credits <= 0:
                    raise ValueError("Credits must be a positive number.")
                # Add the credits to the student object
                student.credits += credits
                # Calculate the quality points and add to the total
                qualityPoints = student.GradeScale(courseGrade) * credits
                # Add the quality points to the student object
                student.totalQualityPoints += qualityPoints
                print(f"Added course with {qualityPoints} quality points and {credits} credits for {student.getFullName()}.")
                print("")
            except ValueError:
                print("Invalid input. Please enter a numeric value for credits.")
                continue
        else:
            print(f"Invalid grade '{courseGrade}'. Please enter a valid grade from the scale (A, A-, B+, B, B-, C+, C, C-, D+, D, F).") 

    # calculate the GPA
    gpa = student.calculateGPA()

    print("-------------------------------------------------------------------------")
    print(f"Current GPA for {student.getFullName()}: {gpa:.2f}") 

if __name__ == "__main__":
    Main()