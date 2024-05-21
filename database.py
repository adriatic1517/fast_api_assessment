
# Note: the module name is psycopg, not psycopg3
import psycopg
import yaml 

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

conn_str = "dbname={dbname} user={user} host={host} password={password}".format(
                                                                    dbname=config['pg']['dbname'], 
                                                                    host = config['pg']['host'],
                                                                    user = config['pg']['user'],
                                                                    password=config['pg']['pwd'])

def create_db():
    with psycopg.connect(conn_str) as conn:

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
    with psycopg.connect(conn_str) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO leads (first_name, last_name, email, state) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, state))
            conn.commit()


def get_all_leads():
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM leads")
            objects = cur.fetchall()
            return objects
                  

    

