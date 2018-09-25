import numpy as np
import psycopg2
import click


def test_connect(dbname, user, password):
    conn = psycopg2.connect(dbname=dbname,
                            host='',
                            port='5439',
                            user=user,
                            password=password)
    print('connected!')
    table_name = 'test.vimbox_pages'
    cur = conn.cursor()
    query_0 = f'select * from {table_name}'
    query_get_users = f'''
    SELECT DISTINCT user_id
    FROM {table_name}
    ORDER BY user_id
    '''
    # users = cur.execute(query_get_users)
    users = cur.execute(query_0)
    print(users)

    cur.close()
    conn.close()


@click.command()
@click.argument('dbname')
@click.argument('user')
@click.argument('password')
def main(dbname, user, password):
    test_connect(dbname, user, password)


if __name__ == '__main__':
    main()
