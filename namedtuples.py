from collections import namedtuple

def average(students):
    return sum([int(x.MARKS) for x in students]) / len(students)
    
if __name__ == '__main__':
    n = int(input())
    col = list(input().split())
    Student = namedtuple('Student', ' '.join(col))
    students = []
    for _ in range(n):
        a, b, c, d = input().split()
        students.append(Student(a, b, c, d))
    
    print(average(students))
