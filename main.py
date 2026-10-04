import psycopg

conn = psycopg.connect("postgresql:///test")

def create_users_table(conn):
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255)
                );
            """)
    conn.commit()

def add_users(conn, users):
    with conn.cursor() as curs:
        curs.executemany(
            "INSERT INTO users (name, email) VALUES (%s, %s);",
            users,
        )
    conn.commit()


def get_all_users(conn):
    with conn.cursor() as curs:
        curs.execute("SELECT id, name, email FROM users;")
        return curs.fetchall()


def main():
    create_users_table(conn)

    add_users(conn, [
        ("Bob", "bob@mail.com"),
        ("Alice", "alice@mail.com"),
        ("John", "john@mail.com"),
    ])

    for raw in get_all_users(conn):
        print(raw)
    
    conn.close()


if __name__ == "__main__":
    main()
