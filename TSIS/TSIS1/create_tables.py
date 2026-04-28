import psycopg2
from config import load_config
def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
            CREATE TABLE groups (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            );
        """,
        """ CREATE TABLE contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                birthday DATE,
                group_id INTEGER,
                CONSTRAINT fk_group
                    FOREIGN KEY (group_id)
                    REFERENCES groups(id)
                    ON DELETE SET NULL
            );
        """,
        """
            CREATE TABLE phones (
                id SERIAL PRIMARY KEY,
                contact_id INTEGER NOT NULL,
                phone VARCHAR(20) NOT NULL,
                type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile')),
                CONSTRAINT fk_contact
                    FOREIGN KEY (contact_id)
                    REFERENCES contacts(id)
                    ON DELETE CASCADE
            );
        """)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__ == '__main__':
    create_tables()