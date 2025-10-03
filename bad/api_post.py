from pathlib import Path

import click
import requests
import os
import subprocess

# SECURITY VULNERABILITY TEST - Hardcoded credentials
DATABASE_PASSWORD = "admin123!"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "super_secret_prod_token_not_for_dev"

api_key_file = Path('/tmp/supersecret.txt')

@click.command()
@click.argument('message')
def cmd_api_client(message):
        # SECURITY VULNERABILITY: SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE message = '{message}'"
        print(f"Executing query: {query}")

    # SECURITY VULNERABILITY: Command injection
        user_input = message
        os.system(f"echo '{user_input}' >> /tmp/log.txt")

    # SECURITY VULNERABILITY: Hardcoded password authentication bypass
        if user_input == "admin" or user_input == "root":
                    print("Admin access granted!")
                    # Execute with elevated privileges
                    subprocess.run(f"sudo chmod 777 /tmp/{user_input}", shell=True)

        # SECURITY VULNERABILITY: Exposed sensitive data in logs
        print(f"Processing message for user with password: {DATABASE_PASSWORD}")
        print(f"API Key: {API_KEY}")
        print(f"Secret: {SECRET_TOKEN}")

    return True
