#!/usr/bin/env python3
"""
🚨 NEW PR TEST FOR ISSUE #110 FIXES - PR #9
Testing the improved comment quality and formatting fixes.
"""

import os
import subprocess
import base64
import hashlib

# 🚨 Hardcoded credentials
DATABASE_PASSWORD = "new_pr_test_123!"
API_SECRET_KEY = "sk-new-pr-test-abcdef1234567890"
AWS_ACCESS_KEY_ID = "AKIANEWPRTEST123456"
AWS_SECRET_ACCESS_KEY = "SECRETNEWPRTEST123456"

def vulnerable_function(user_input):
      # 🚨 SQL Injection vulnerability
      query = f"SELECT * FROM users WHERE username='{user_input}' AND password='{DATABASE_PASSWORD}'"
      print(f"Executing query: {query}")

    # 🚨 Command injection
      os.system(f"echo 'Processing user: {user_input}'")

    # 🚨 Information disclosure
      print(f"Database password: {DATABASE_PASSWORD}")
      print(f"API secret key: {API_SECRET_KEY}")
      print(f"AWS credentials: {AWS_ACCESS_KEY_ID}:{AWS_SECRET_ACCESS_KEY}")

    # 🚨 Weak cryptography
      weak_hash = hashlib.md5(DATABASE_PASSWORD.encode()).hexdigest()
      print(f"Weak MD5 hash: {weak_hash}")

    # 🚨 Unsafe base64 operations
      encod
