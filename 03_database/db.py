import psycopg2

import os

DB_HOST=os.getenv('DB_HOST', 'localhost')

create_sequence = """
CREATE SEQUENCE IF NOT EXISTS serial;
"""

create_table = """
CREATE TABLE IF NOT EXISTS values(
    id integer PRIMARY KEY DEFAULT nextval('serial'),
    value varchar(255)
);
"""

insert_values= """
INSERT INTO values (value) VALUES (\'FOO\');
INSERT INTO values (value) VALUES (\'BAR\');
INSERT INTO values (value) VALUES (\'BAZ\');
"""

connection = psycopg2.connect(f"host={DB_HOST} dbname=postgres user=postgres password=mysecretpassword")
cursor = connection.cursor()
cursor.execute(create_sequence)
cursor.execute(create_table)
cursor.execute(insert_values)
cursor.execute("SELECT value FROM values;")
print([value[0] for value in cursor.fetchall()])
connection.commit()
