if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
 
# Getting only score values 
scores = [i[1] for i in students ]

# sorting and get second lowest unique score 
second_lowest = sorted(list(set(scores)))[1]

# Getting names with second lowest unique score
names = []
for i in range(len(students)):
    if students[i][1] == second_lowest:
        names.append(students[i][0])

# Sorting Names
names =  sorted(names)
names

# Printing Sorted Names
for i in names:
    print(i)
        
