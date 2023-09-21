import psycopg2
from sql_config import host, db_name, user, password

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # commands
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT hotel FROM hotels WHERE City = 'Nizniy Novgorod';"""
        )
        result_code = cursor.fetchmany(10000)
        print('[INFO] COD Completed.')

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostreSQL connection closed')