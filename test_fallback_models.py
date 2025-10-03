#!/usr/bin/env python3
"""
🚨 FALLBACK MODEL TEST - PR #7
Testing if fallback LLM models are working properly.
"""

import os
import subprocess

# 🚨 Hardcoded credentials
DATABASE_PASSWORD = "fallback_test_123!"
AWS_ACCESS_KEY = "AKIAFALLBACKTEST123456"
SECRET_TOKEN = "sk-fallback-test-abcdef1234567890"

def vulnerable_function(user_input):
      # 🚨 SQL Injection vulnerability
      query = f"SELECT * FROM users WHERE username='{user_input}' AND password='{DATABASE_PASSWORD}'"
      print(f"Executing query: {query}")

    # 🚨 Command injection
      os.system(f"echo 'User input: {user_input}'")

    # 🚨 Information disclosure
      print(f"Database password: {DATABASE_PASSWORD}")
      print(f"AWS key: {AWS_ACCESS_KEY}")
      print(f"Secret token: {SECRET_TOKEN}")

    return "Vulnerable function executed"

if __name__ == "__main__":
      vulnerable_function("admin")
