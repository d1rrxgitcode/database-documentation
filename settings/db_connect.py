import psycopg2

from settings.config import settings

conn = psycopg2.connect(
    database=settings.db_name,
    user=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port
)