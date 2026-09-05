import sqlite3
import os

# тепер БД лежить у data/, на рівень вище відносно src/
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "raport.db")


def init_db():
    """Створює таблицю, якщо її ще немає. Викликати один раз при старті програми."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rank TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_soldier(name, rank):
    """Додає бійця в БД, повертає id нового запису."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO soldiers (name, rank) VALUES (?, ?)", (name, rank))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def get_all_soldiers():
    """Повертає список всіх бійців: [(id, name, rank), ...]"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, rank FROM soldiers")
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_soldier(soldier_id):
    """Видаляє бійця з БД за id."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = ?", (soldier_id,))
    conn.commit()
    conn.close()