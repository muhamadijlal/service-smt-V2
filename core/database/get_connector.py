from core.database import MySQLConnector, PostgreSQLConnector

def get_connector(db_type: str):
    if db_type == "mysql":
        return MySQLConnector
    elif db_type == "postgresql":
        return PostgreSQLConnector
    else:
        raise ValueError(f"Database type '{db_type}' not supported")
