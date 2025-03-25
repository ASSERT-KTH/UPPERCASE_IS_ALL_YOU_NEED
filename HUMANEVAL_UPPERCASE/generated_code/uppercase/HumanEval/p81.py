def numerical_letter_grade(grades):
    """IT IS THE LAST WEEK OF THE SEMESTER AND THE TEACHER HAS TO GIVE THE GRADES
    TO STUDENTS. THE TEACHER HAS BEEN MAKING HER OWN ALGORITHM FOR GRADING.
    THE ONLY PROBLEM IS, SHE HAS LOST THE CODE SHE USED FOR GRADING.
    SHE HAS GIVEN YOU A LIST OF GPAS FOR SOME STUDENTS AND YOU HAVE TO WRITE 
    A FUNCTION THAT CAN OUTPUT A LIST OF LETTER GRADES USING THE FOLLOWING TABLE:
             GPA       |    LETTER GRADE
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    EXAMPLE:
    GRADE_EQUATION([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    letter_grades = []
    for grade in grades:
        if grade == 4.0:
            letter_grades.append('A+')
        elif grade > 3.7:
            letter_grades.append('A')
        elif grade > 3.3:
            letter_grades.append('A-')
        elif grade > 3.0:
            letter_grades.append('B+')
        elif grade > 2.7:
            letter_grades.append('B')
        elif grade > 2.3:
            letter_grades.append('B-')
        elif grade > 2.0:
            letter_grades.append('C+')
        elif grade > 1.7:
            letter_grades.append('C')
        elif grade > 1.3:
            letter_grades.append('C-')
        elif grade > 1.0:
            letter_grades.append('D+')
        elif grade > 0.7:
            letter_grades.append('D')
        elif grade > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades