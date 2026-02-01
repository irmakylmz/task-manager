import sqlite3


def connect_db():
    return sqlite3.connect("../app.db")


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_name TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    conn.commit()
    conn.close()


def add_user(username):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        print(f"Kullanıcı '{username}' başarıyla oluşturuldu.")
    except sqlite3.IntegrityError:
        print("Bu kullanıcı zaten var.")
    finally:
        conn.close()


def add_task(user_id, task):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (user_id, task_name) VALUES (?, ?)",
        (user_id, task)
    )

    conn.commit()
    conn.close()
    print("Görev eklendi.")


def get_tasks(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT task_name FROM tasks WHERE user_id = ?",
        (user_id,)
    )

    tasks = cursor.fetchall()
    conn.close()
    return tasks