
# Note: the module name is psycopg, not psycopg3
import psycopg


def create_db():
    with psycopg.connect("dbname=postgres user=postgres host=127.0.0.1 password=postgres") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id serial PRIMARY KEY,
                    first_name text,
                    last_name text,
                    email text,
                    state text
                        )
                """)
            conn.commit()

def add_lead(first_name, last_name, email, state):
    with psycopg.connect("dbname=postgres user=postgres host=127.0.0.1 password=postgres") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO leads (first_name, last_name, email, state) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, state))
            conn.commit()


def get_all_leads():
    with psycopg.connect("dbname=postgres user=postgres host=127.0.0.1 password=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM leads")
            objects = cur.fetchall()
            return objects
                  

    

