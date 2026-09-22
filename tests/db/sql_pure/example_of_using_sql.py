q = '''
CREATE TABLE IF NOT EXISTS public.user_table_2 (
	id int4 GENERATED ALWAYS AS IDENTITY NOT NULL,
	name varchar NOT NULL,
	description varchar NULL,
	CONSTRAINT user_table_2_pk PRIMARY KEY (id)
);
'''

'''CREATE TABLE public.user_address (
	user_id int4 NOT NULL,
	address varchar NOT NULL,
	CONSTRAINT user_address_pk PRIMARY KEY (user_id),
	CONSTRAINT user_address_user_table_2_fk FOREIGN KEY (user_id) REFERENCES public.user_table_2(id) ON DELETE CASCADE ON UPDATE CASCADE
);


insert into user_address (user_id, address)
values (12, 'Ukraine, 69001')

insert into user_address (user_id, address)
values (26, 'Ukraine, Kyiv')

select u.name, a.address
from user_table_2 u join user_address a on u.id  = a.user_id

'''

# connector, cursor

import psycopg2 as ps

from faker import Faker

faker = Faker()

connector = ps.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="postgres",
    password="den",
)

cursor = connector.cursor()

for _ in range(10):
    insert_q = f'''
    INSERT INTO public.user_table_2 (name, description) VALUES ('{faker.name()}', '{faker.job()}')'''


    cursor.execute(insert_q)

update_q = f'''
update public.user_table_2
set description = 'updated description'
where id > 4 and id < 11
'''


cursor.execute(update_q)

delete_q = '''
DELETE 
FROM public.user_table_2
where id between 15 and 25
'''

cursor.execute(delete_q)

connector.commit()

