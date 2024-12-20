import os
import sys
from django.db import connections, OperationalError
from psycopg2 import connect
from psycopg2.errors import DuplicateDatabase

def create_database():
    """Automatically creates the database if it doesn't exist."""
    from django.conf import settings

    db_settings = settings.DATABASES['default']

    if db_settings['ENGINE'] == 'django.db.backends.postgresql':
        db_name = db_settings['NAME']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_host = db_settings['HOST']
        db_port = db_settings['PORT']

        try:
            # Connect to PostgreSQL with the default database
            conn = connect(
                dbname="postgres",  # Connect to the default PostgreSQL database
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            conn.autocommit = True
            cursor = conn.cursor()

            # Attempt to create the database
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")
            cursor.close()
            conn.close()

        except DuplicateDatabase:
            print(f"Database '{db_name}' already exists.")
        except Exception as e:
            print(f"Error creating database: {e}")
            sys.exit(1)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whistly.settings')

    # Try connecting to the database
    try:
        connection = connections['default']
        connection.cursor()
    except OperationalError:
        print("Database does not exist, attempting to create...")
        create_database()

    # Proceed with Django commands
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()
