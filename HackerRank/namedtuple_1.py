from collections import namedtuple
n, Grades = int(input()), namedtuple('Grades', input())
grade_list = [float((Grades(*list(input().split()))).MARKS) for _ in range(n)]
print( '{:.2f}'.format(sum(grade_list)/n))