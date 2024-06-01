from scheme import factory
from scheme import Employee, Project, Category

session = factory()

e = session.query(Employee).where(Employee.last_name == "Richard").first()


p1 = Project()
p1.name = "IronMuscles"

c1 = session.query(Category).where(Category.name == "Health").first()
p1.categories.append(c1)

e.projects.append(p1)

p2 = Project()
p2.name = "SonsOfMoney"

c2 = session.query(Category).where(Category.name == "Banking").first()
p2.categories.append(c2)

e.projects.append(p2)

session.commit()
