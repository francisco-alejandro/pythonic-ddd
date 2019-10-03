import os

def get_postgres_uri():
    host = os.getenv('PG_HOST', 'localhost')
    port = int(os.getenv('DB_PORT', '5432'))
    password = os.getenv('PG_PASSWORD', 'postgres')
    user = os.getenv('PG_USER', 'postgres')
    db_name = os.getenv('PG_DATABASE', 'payment')

    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'