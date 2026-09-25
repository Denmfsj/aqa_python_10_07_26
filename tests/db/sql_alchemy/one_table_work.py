from sqlalchemy import create_engine, select, or_, and_
from sqlalchemy.orm import sessionmaker
from core.db.sqlalchemy.user_table import User
from core.db.sqlalchemy.base_class import Base
from faker import Faker
import random

faker = Faker()


# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
DATABASE_URL = "postgresql://postgres:den@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


user_john = User(name="john", age=32)  # instance = row

users = []
for _ in range(5):
    users.append(User(name=faker.name(), age=random.choice(range(18, 100))))


 # додати строку
session.add_all(users)
session.commit()

# # Оновлення інформації про користувача
# users = session.query(User).filter_by(age=32).all()  # filter = where
# print(*users, sep='\n')
#
# user_number_2 = users[1]
# user_number_2.name = 'Alex'
#
#
# session.commit()

select_q = select(User).where(User.age < 30).where(User.name.endswith('s'))  # підготовки sql запита
# SELECT * FROM User
# WHERE age < 30 AND name endswith s
result = session.execute(select_q)  # надсилання select_q і отримання результату

users = [k[0] for k in result.fetchall()]  # fetchall() - витягує дані з result

# for u in users:
#     print(f'User {u.name} is {u.age} years old')


# select * from User where id > 40 and (age < 30 or endswith s )
select_q = select(User).where(
    and_(User.id > 40,   # id > 40 and
         or_(User.age < 30, User.name.endswith('s'))) # age < 30 OR name endswith s
)
result = session.execute(select_q)

users = [k[0] for k in result.fetchall()]  # fetchall() - витягує дані з result
# for u in users:
#     print(u)

data = session.query(User).order_by(User.age).all()  # order_by = order by age asc
data = session.query(User).order_by(User.age.desc()).all()  # order_by = order by desc asc
print(*data, sep='\n')