n = int(input())
student_marks = {}

# Read the student names and their scores
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

# Read the student name to query
query_name = input()

# Calculate the average of the marks for the queried student
query_scores = student_marks[query_name]
average_score = sum(query_scores) / len(query_scores)

# Print the average score formatted to 2 decimal places
print(f"{average_score:.2f}")
