import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    bot TEXT
)
""")

def save_chat(user, bot):
    cursor.execute("INSERT INTO chats (user, bot) VALUES (?, ?)", (user, bot))
    conn.commit()

def get_chats():
    cursor.execute("SELECT * FROM chats")
    return cursor.fetchall()