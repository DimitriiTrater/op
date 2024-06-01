from scheme import factory
from scheme import Employee, Project, Category

session = factory()

e = session.query(Employee).where(Employee.first_name == "Michel").first()

for p in e.projects:
    session.delete(p)

session.delete(e)

session.commit()
