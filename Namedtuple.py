from collections import namedtuple
n=int(input())
student=namedtuple('student',input())
students = [student(*input().split()) for i in range(n)]
print("{:.2f}".format(sum(float(s.MARKS) for s in students) / n))
