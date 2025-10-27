import requests
import sqlite3

# New vulnerable code (ADDED LINE - Tier 1)
def search_users(username, cursor):
    query = f"SELECT * FROM users WHERE name = '{username}'"  # SQL Injection
    cursor.execute(query)
    return cursor.fetchall()


# Existing vulnerable code (CONTEXT LINE - Tier 2)
def get_user_posts(username):
    r = requests.get(f'http://127.0.0.1:5000/api/post/{username}')  # SSRF
    return r.json()

# Modified safe code (ADDED LINE - No vuln)
def safe_function():
    return "Hello World"
