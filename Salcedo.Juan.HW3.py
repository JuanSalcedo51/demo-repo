'''A request is being made to create a program where the user is asked to enter their grades for homework,quizzes, labs, and exams,
so that the user receives the average for each, the percentage corresponding to the final grade, the final grade, and their letter grade,
all in a readable format.'''

'''Define the list of grades for each category, in this case, the task grades,
where the user will be asked to enter their grades separated by commas, then,
the code will automatically accept the comma as a separator that will divide the code,
where then, each substring formed will be converted to float and output as a list.'''

def get_homework_grades(): #For Homeworks.
    homework_grades = input("Enter your homework grades (separated by commas): ")
    hw_grades_comma = homework_grades.split(",") #The string will split by the commas.
    hw_grades_list = [float(number) for number in hw_grades_comma] #The brackets will be responsible for converting the floats into a list.
    #"for number" is making a variable for each grade, "in hw_grades_comma" represent where the number is obtained.
    return(hw_grades_list)

'''For the average of each category, the previous function is invoked,
since it contains the list of grades, the sum() commands are used so that all the grades in the list are added together,
and len() to define the number of grades within the list,
then the sum of the grades (sum) will be divided by their quantity (len) thus obtaining the average,
and thanks to the fact that it uses floats, there will be no problems regarding decimals.'''

hw_total = get_homework_grades() #Invoke previous function.
sum_hw = sum(hw_total) #Summatory of grades.
len_hw = len(hw_total) #Amount of grades.
hw_average = sum_hw / len_hw #Average formula.

'''The process is repeated again for each category, replacing the variables appropriately.'''

def get_quiz_grades(): #For Quizzes.
    quiz_grades = input("Enter your quiz grades (separated by commas): ")
    qz_grades_comma = quiz_grades.split(",")
    qz_grades_list = [float(number) for number in qz_grades_comma]
    return(qz_grades_list)

qz_total = get_quiz_grades()
sum_qz = sum(qz_total)
len_qz = len(qz_total)
qz_average = sum_qz / len_qz

def get_lab_grades(): #For Labs.
    lab_grades = input("Enter your lab grades (separated by commas): ")
    lb_grades_comma = lab_grades.split(",")
    lb_grades_list = [float(number) for number in lb_grades_comma]
    return(lb_grades_list)

lb_total = get_lab_grades()
sum_lb = sum(lb_total)
len_lb = len(lb_total)
lb_average = sum_lb / len_lb

def get_exam_grades(): #For Exams.
    exam_grades = input("Enter your exam grades (separated by commas): ")
    ex_grades_comma = exam_grades.split(",")
    ex_grades_list = [float(number) for number in ex_grades_comma]
    return(ex_grades_list)

ex_total = get_exam_grades()
sum_ex = sum(ex_total)
len_ex = len(ex_total)
ex_average = sum_ex / len_ex

'''Since each average is represented with a certain percentage of the total,
a function is created that determines the value of each average in the percentage for the total,
that is, of the average obtained from a category, how much will it contribute to the final grade?'''

def calculate_grade(hw_average, qz_average, lb_average, ex_average): #The averages is invoked in the function.
    percentage_hw = hw_average * 0.30 #For Homeworks the percentage is 30% of the total.
    percentage_qz = qz_average * 0.10 #For Quizzes the percentage is 10% of the total.
    percentage_lb = lb_average * 0.10 #For Labs the percentage is 10% of the total.
    percentage_ex = ex_average * 0.50 #For Exams the percentage is 50% of the total.
    return(percentage_hw, percentage_qz, percentage_lb, percentage_ex)

#Previous function is invoked.
percentage_hw, percentage_qz, percentage_lb, percentage_ex = calculate_grade(hw_average, qz_average, lb_average, ex_average)

'''The total grade is the sum of all the percentages obtained previously, so the previous function had to be called.'''
total_grade = percentage_hw + percentage_qz + percentage_lb + percentage_ex

'''To define the grade (letter) of the total grade,
a function is defined that creates grade ranges and determines the letter for the final grade,
using as a reference the grading scale used by FAU.'''
def grade_scale():
    if 94<= total_grade <=100: #For example, if the total grade is between the range of 94 to 100, then the letter will be A.
        return "A"
    elif 90 <= total_grade <= 93: #Else, if the total grade is between 90 to 93, then the letter will be A- and continue down.
        return "A-"
    elif 87 <= total_grade <= 89:
        return "B+"
    elif 84 <= total_grade <= 86:
        return "B"
    elif 80 <= total_grade <= 83:
        return "B-"
    elif 77 <= total_grade <= 79:
        return "C+"
    elif 74 <= total_grade <= 76:
        return "C"
    elif 70 <= total_grade <= 73:
        return "C-"
    elif 67 <= total_grade <= 69:
        return "D+"
    elif 64 <= total_grade <= 66:
        return "D"
    elif 61 <= total_grade <= 63:
        return "D-"
    else:
        return "F" #Here, if the final note is under the previous range (61 to 63) or is less than 60, the letter will be F
    
grades = grade_scale() #The previous function is called again

sections = ("-"*110) #For organize the output, sections will make separators represented by - for separate sections for grade report
space = " " #A space is defined for format purposes

'''The report of grades is printed organized and separated, for greater readability.'''

print(space)
print(f"GRADES REPORT\n{sections}") #Tittle and first section

'''First section is about the average of each category'''

#List of Homework grades, sum, amount and average using one decimal.
print(f"Homework grades{space:^1}:{space:^1}{hw_total} = {sum_hw}/{len_hw} = {hw_average:.1f}")

#List of Quizzes grades, sum, amount and average using one decimal.
print(f"Quiz grades{space:^5}:{space:^1}{qz_total} = {sum_qz}/{len_qz} = {qz_average:.1f}")

#List of Labs grades, sum, amount and average using one decimal.
print(f"Lab grades{space:^6}:{space:^1}{lb_total} = {sum_lb}/{len_lb} = {lb_average:.1f}")

#List of Exam grades, sum, amount and average using one decimal. Second section is added.
print(f"Exam grades{space:^5}:{space:^1}{ex_total} = {sum_ex}/{len_ex} = {ex_average:.1f}\n{sections}")

'''Second section is about the percentage of each average.'''

#Subtitle Homework, separated and format by spaces, it includes average using one decimal, by 30% and output the percentage.
print(f"Homeworks {space:^3}: {space:^2} {hw_average:.1f} x 0.30 = {percentage_hw:.1f}")

#Subtitle Quizzes, separated and format by spaces, it includes average using one decimal, by 10% and output the percentage.
print(f"Quizzes {space:^5}: {space:^2} {qz_average:.1f} x 0.10 = {percentage_qz:.1f}")

#Subtitle Labs, separated and format by spaces, it includes average using one decimal, by 10% and output the percentage.
print(f"Labs {space:^8}: {space:^2} {lb_average:.1f} x 0.10 = {percentage_lb:.1f}")

#Subtitle Exams, separated and format by spaces, it includes average using one decimal, by 50% and output the percentage.
#Third section is added.
print(f"Exams {space:^7}: {space:^2} {ex_average:.1f} x 0.50 = {percentage_ex:.1f}\n{sections}")

'''This section the total is printed, format properly.'''

print(f"TOTAL{space:^4}:{space:^2}{total_grade:.1f}\n{sections}") #Total output with just one decimal, fourth section is added.

'''The last section is the grade or letter of the total'''
print(f"GRADE{space:^4}:{space:^2}{grades}\n{sections}") #Grade output, format properly, last section or final separator.
