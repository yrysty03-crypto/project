from config import load_config
import psycopg2

def get_connection():
    try:
        config = load_config()   # <-- добавили
        conn = psycopg2.connect(**config)
        print('Connected to PostgreSQL')
        return conn
    except Exception as error:
        print(error)
if __name__ == '__main__':
    config = load_config()
    get_connection()