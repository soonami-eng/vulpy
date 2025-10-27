import requests
import sqlite3

# This SSRF already exists (context line)
def get_data(url):
    return requests.get(f'http://127.0.0.1/{url}')

# NEW: SQL injection (added line)
def search(name, cursor):
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    return cursor.fetchall()
