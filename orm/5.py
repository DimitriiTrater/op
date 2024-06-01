from scheme import factory
from scheme import Employee, Project, Category

session = factory()

e = session.query(Employee).where(Employee.last_name == "Richard").first()

for p in e.projects:
    print(p)
    print("Category:", end=" ")
    for c in p.categories:
        print(c.name, end=" ")
    print("leader_of_project:", p.leader_of_project)
