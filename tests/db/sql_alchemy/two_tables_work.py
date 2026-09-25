from sqlalchemy import create_engine, select, or_, and_
from sqlalchemy.orm import sessionmaker
from core.db.sqlalchemy.dep_table import Department
from core.db.sqlalchemy.emp_table import Employee
from core.db.sqlalchemy.base_class import Base
from faker import Faker
import random
from definitions import SQLITE_DB_FOLDER

faker = Faker()


# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
# DATABASE_URL = "postgresql://postgres:den@localhost:5432/postgres"
DATABASE_URL = f"sqlite:///{SQLITE_DB_FOLDER}"
engine = create_engine(DATABASE_URL)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_and_create_if_not_exist_dep(dep_name):


    devops_dep = Department(name=dep_name)  # я створюю row локально для департамента з ім'ям dep_name

    # шукаю в бд чи є такий
    existed_devops_dep = session.query(Department).filter_by(name=devops_dep.name).first()

    # створить DevOps якщо його нема
    if not existed_devops_dep:
        session.add(devops_dep)
        session.commit()
    else:
        devops_dep = existed_devops_dep

    return devops_dep

for k in ('DevOps', 'HR', 'QA'):
    new_dep = get_and_create_if_not_exist_dep(k)
    print(new_dep.id, new_dep.name)

hr_dep = session.query(Department).filter_by(name='HR').first() # визначили строку(!) of table Department
emp = Employee(name=faker.name(), department=hr_dep) # ствою нового юзера вказучі строку(!) з таблиці Department

session.add(emp)
session.commit()

hr_emps =  session.query(Employee).all()
for emp in hr_emps:

    # print(emp.name, '|', emp.department)
    print(emp.name, 'is working in', emp.department.name)  # emp.departament - це строка з таблиці Department
