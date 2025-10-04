#!/usr/bin/env python3
"""
🚨 ISSUE #110 FIXES TEST - PR #9
Testing the improved comment quality and formatting fixes.
"""

import os
import subprocess
import base64
import hashlib

# 🚨 Hardcoded credentials
DATABASE_PASSWORD = "issue_110_test_123!"
API_SECRET_KEY = "sk-issue110-test-abcdef1234567890"
AWS_ACCESS_KEY_ID = "AKIAISSUE110TEST123456"
AWS_SECRET_ACCESS_KEY = "SECRETISSUE110TEST123456"

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
      encoded = base64.b64encode(b"malicious_payload").decode()
      decoded = base64.b64decode(encoded)
      p
