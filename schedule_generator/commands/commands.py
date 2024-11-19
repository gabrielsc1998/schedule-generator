def clear_db():
    print('Cleaning database...')
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute('SET FOREIGN KEY_CHECKS = 0')
        cursor.execute('SHOW TABLES')
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f'TRUNCATE TABLE {table[0]}')
        cursor.execute('SET FOREIGN KEY_CHECKS = 1')
    print('Database cleaned')
