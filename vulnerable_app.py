import os
import sqlite3
import subprocess

# Hardcoded secrets - security vulnerability
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_PASSWORD = "admin123"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
    
    # SQL Injection vulnerability
    def get_user(self, username):
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    # SQL Injection vulnerability
    def authenticate(self, username, password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(query)
        return self.cursor.fetchone() is not None

# Command Injection vulnerability
def run_system_command(user_input):
    command = "ping -c 4 " + user_input
    os.system(command)

# Use of eval - code injection vulnerability
def calculate(expression):
    result = eval(expression)
    return result

# Insecure deserialization
import pickle

def load_user_data(data):
    user_obj = pickle.loads(data)
    return user_obj

# Weak cryptography
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Path traversal vulnerability
def read_file(filename):
    with open("/var/www/files/" + filename, 'r') as f:
        return f.read()

# Subprocess with shell=True
def execute_command(cmd):
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    # Example usage
    db = UserDatabase()
    user = db.get_user("admin")
    run_system_command("google.com")
    result = calculate("2 + 2")
    print(f"Result: {result}")
