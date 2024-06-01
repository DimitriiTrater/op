from sqlalchemy import(
    create_engine,
    Column,
    ForeignKey,
    CheckConstraint,
    Integer,
    String,
    Boolean,
    Numeric,
    SmallInteger
)

from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Basis(DeclarativeBase):
    ...

class Employee(Basis):
    __tablename__ = "employees"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)

    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)

    grade = Column(Integer(), ForeignKey("grades.id"))
    projects = relationship("Project", back_populates="leader_of_project")

    def __str__(self):
        return f"<{self.id}> {self.last_name} {self.email} {self.phone} {self.grade} {self.projects}"

    def __repr__(self):
        return f"{self.last_name} {self.email} {self.phone}"

class Grade(Basis):
    __tablename__ = "grades"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    grade = Column(String(20), nullable=False, unique=True)
    salary = Column(Integer(), nullable=False)

    def __str__(self):
        return f"<{self.id}> {self.grade} {self.salary}"

    def __repr__(self):
        return f"{self.grade} {self.salary}"

class Project(Basis):
    __tablename__ = "projects"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    leader_of_project_id = Column(Integer(), ForeignKey("employees.id"))
    leader_of_project = relationship("Employee", back_populates="projects")

    categories = relationship("Category", back_populates="projects",
                              secondary="projects_categories")

    def __str__(self):
        return f"<{self.id}> {self.name} {self.leader_of_project_id}"

    def __repr__(self):
        return f"{self.name} {self.leader_of_project_id}"

class Category(Basis):
    __tablename__ = "categories"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    projects = relationship("Project", back_populates="categories",
                            secondary="projects_categories")

class ProjectCategory(Basis):
    __tablename__ = "projects_categories"
    project_id = Column(Integer(), ForeignKey("projects.id"), primary_key=True)
    category_id = Column(Integer(), ForeignKey("categories.id"), primary_key=True)

engine = create_engine("sqlite:///staff.db?echo=True")

Basis.metadata.create_all(engine)

factory = sessionmaker(bind=engine)
