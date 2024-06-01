from scheme import factory
from scheme import Employee, Project, Category

session = factory()

e = session.query(Employee).where(Employee.last_name == "Richard").first()

e.first_name = "Richard"
e.last_name = "Stallman"

session.commit()
