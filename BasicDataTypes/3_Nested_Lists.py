if __name__ == '__main__':
    List=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        List.append([name,score])
    unique_grades=[]
    for student in List:
        grade = student[1]
        if grade not in unique_grades:
            unique_grades.append(grade)
    unique_grades.sort()
    second_lowest= unique_grades[1]
    second_lowest_students=[student[0] for student in List if student[1]==second_lowest]
    second_lowest_students.sort()
    for i in second_lowest_students:
        print(i)
