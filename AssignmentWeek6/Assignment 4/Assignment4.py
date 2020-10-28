eren = {
  "name": "Eren",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
mikasa = {
 "name": "Mikasa",
 "homework": [100.0, 92.0, 98.0, 100.0],
 "quizzes": [82.0, 83.0, 91.0],
 "tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

#Put each students into list
students = [eren, mikasa, armin]

#Print all of the information of each student
for student in students:
    print("name:",student["name"])
    print("homework:",student["homework"])
    print("quizzes:",student["quizzes"])
    print("tests:",student["tests"],"\n---------------------------------")

def average (numbers):
    total = sum(numbers)
    total = float(total)
    result = total/len(numbers)
    return result

def get_average (student):
    homework = average(student.get("homework"))
    quizzes = average(student.get("quizzes"))
    tests = average(student.get("tests"))
    result = homework*0.1 + quizzes*0.3 + tests*0.6
    return result 


def get_letter_grade (score):
    if(score>=90):
        return "A"
    elif(score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "C"
    else:
        return "F"

#UNCOMMENT THE CODE BELOW TO PRINT EACH STUDENT'S AVERAGE SCORE AND GRADE

# for student in students:
#     print(student["name"]+"'s average score:",get_average(student),"\n"+student["name"]+"'s grade:",get_letter_grade(get_average (student)))

def get_class_average (students):
    results = []
    for student in students:
        results.append(get_average(student))
    result = average(results)
    return result
print("Class's Average:",get_class_average(students))
print("Class's Grade:",get_letter_grade(get_class_average(students)))