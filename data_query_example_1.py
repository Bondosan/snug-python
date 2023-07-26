from get_odbc_connection import get_connections

def main():
    connections = get_connections()
    test_connection = connections.get('test')

    query = """
        select first, last, id
        from hr_table
        where id = '33'
        """
    
    with test_connection.get_connection() as conn:    
        data = conn.cursor().execute(query).fetchall()

    for row in data:
        print(row.first, row.last, row.id, sep='\n')


if __name__ == "__main__":
    main()