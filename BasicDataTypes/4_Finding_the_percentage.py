if __name__ == '__main__':
    avg=0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        for mark in student_marks[query_name]:
            avg+=mark
        avg=avg/len(student_marks[query_name])
    print(f"{avg:.2f}")
