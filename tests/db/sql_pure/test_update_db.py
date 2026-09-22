import psycopg2 as ps
from faker import Faker
import pytest

from definitions import BASE_FOLDER

faker = Faker()

# precondition: connect to db, generate data

# test: потрібно вставити нового юзера і перевірити, що у нього вірне ім'я(яке ми хотіли)

# postcondition, delete data, close connection


@pytest.fixture
def connection_and_cursor():
    # connector = ps.connect(BASE_FOLDER/'test.db')
    connector = ps.connect(
        host="localhost",
        port="5432",
        dbname="postgres",
        user="postgres",
        password="den",
    )


    connector.connect()
    cursor = connector.cursor()

    yield connector, cursor

    cursor.close()
    connector.close()

@pytest.fixture
def generate_user_data():
    user_name = faker.name().replace("'", "")
    user_job = faker.job().replace("'", "")

    return user_name, user_job

@pytest.fixture
def insert_and_delete_data(connection_and_cursor, generate_user_data):
    connector, cursor = connection_and_cursor
    user_name, user_job = generate_user_data

    q = f'''INSERT INTO public.user_table_2 (name, description) 
            VALUES ('{user_name}', '{user_job}') 
            RETURNING id'''
    cursor.execute(q)
    user_id = cursor.fetchone()[0]
    connector.commit()

    yield user_id

    cursor.execute(f"""DELETE FROM public.user_table_2 WHERE id = {user_id}""")
    connector.commit()




def test_data_was_inserted(generate_user_data, insert_and_delete_data,
                           connection_and_cursor):

    _, cursor = connection_and_cursor
    expected_user_name, _ = generate_user_data
    user_id = insert_and_delete_data

    q = f"""
    select id, name, description 
    from public.user_table_2 
    where id = '{user_id}'"""

    cursor.execute(q)

    # [(col_1, col_2, ...), (....), (....), .., row(n-1), row(n), ...]
    users = cursor.fetchall()  # [(id, name, description ), (id, name, description ), (....)]

    assert len(users) == 1, f'Expected only 1 user with id = {user_id} but db returns {len(users)}'

    user = users[0]  # tuple(id, name, description)
    _, actual_user_name, _ = user
    assert expected_user_name == actual_user_name,\
        f'Expected user name is {expected_user_name} but actual is {actual_user_name}'

