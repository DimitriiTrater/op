from scheme import factory
from scheme import Category


session = factory()

cats = ["Banking", "Health", "Sport", "Maps"]

for cat in cats:
    c = Category(name=cat)
    session.add(c)

session.commit()
