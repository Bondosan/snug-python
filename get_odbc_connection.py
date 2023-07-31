import csv
import pyodbc
from pathlib import Path


class Connection:
    def __init__(self, server: str, database: str, user: str, password: str):
        self.server = server
        self.database = database
        self.user = user
        self.password = password

    def get_connection(self):
        connection_string = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={self.server};
        DATABASE={self.database};
        UID={self.user};
        PWD={self.password};
        Encrypt=yes;
        TrustServerCertificate=yes"""
        return pyodbc.connect(connection_string)


def load_connection_csv(file_path: str) -> dict:
    connections = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            connection = Connection(
                row["server"],
                row["database"],
                row["user"],
                row["password"]
            )
            connections[row["name"]] = connection

    return connections


def get_connections() -> dict:
    csv_path = f"{Path(__file__).parent.resolve()}\\connections.csv"
    connections = load_connection_csv(csv_path)
    return connections
