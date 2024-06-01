from scheme import factory
from scheme import Employee, Grade

session = factory()

g = 2

e1 = Employee(
    last_name="Richard",
    first_name="Mark",
    phone="+98727347321",
    email="prikool@uan.dt",
    grade=g
)

e2 = Employee(
    last_name="Linus",
    first_name="Tesla",
    phone="+387223345",
    email="dog@cat.mouse",
    grade=g
)

e3 = Employee(
    last_name="Omar",
    first_name="Miami",
    phone="+1222223333",
    email="xmas@mall.uin",
    grade=g
)

session.add_all([e1, e2, e3])
session.commit()
