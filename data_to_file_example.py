import csv
from get_odbc_connection import get_connections


def main():
    connections = get_connections()
    test_connection = connections.get('test')

    csv_header_row = ["First Name", "Last Name", "ID"]

    query = """
        select first, last, id
        from hr_table
        """

    with test_connection.get_connection() as conn:
        data = conn.cursor().execute(query).fetchall()

    with open('testout.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(csv_header_row)
        csv_writer.writerows(data)


if __name__ == "__main__":
    main()
