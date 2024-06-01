# The script is creating grades and adding only one employee
# Also, the script is making projects for that employee
from scheme import factory
from scheme import Employee, Grade, Project

j = Grade(grade="Junior", salary=700)
m = Grade(grade="Middle", salary=1400)
s = Grade(grade="Senior", salary=2800)

session = factory()
session.add(j)
session.add(m)
session.add(s)
session.commit()


p1 = Project(name="astar")
p2 = Project(name="DUModel")

m = Employee()
m.first_name = "Michel"
m.last_name = "Dyakovski"
m.middle_name = "Jacob"
m.phone = "1234213"
m.email = "email"
m.grade = j.id

m.projects = [p1, p2]

print(m)

session.add(m)
session.commit()

print(m)
