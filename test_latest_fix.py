#!/usr/bin/env python3
"""
🚨 LATEST FIX TEST - PR #8
Testing the latest fallback model fix.
"""

import os
import subprocess
import base64
import hashlib

# 🚨 Hardcoded credentials
SECRET_KEY = "latest_fix_test_123!"
API_TOKEN = "sk-latest-fix-test-abcdef1234567890"
AWS_ACCESS_KEY = "AKIALATESTFIXTEST123456"

def vulnerable_function(user_input):
      # 🚨 SQL Injection vulnerability
      query = f"SELECT * FROM users WHERE name='{user_input}' AND secret='{SECRET_KEY}'"
      print(f"Executing query: {query}")

    # 🚨 Command injection
      os.system(f"echo 'Processing user: {user_input}'")

    # 🚨 Information disclosure
      print(f"Secret key: {SECRET_KEY}")
      print(f"API token: {API_TOKEN}")
      print(f"AWS access key: {AWS_ACCESS_KEY}")

    # 🚨 Weak cryptography
      weak_hash = hashlib.md5(SECRET_KEY.encode()).hexdigest()
      print(f"Weak MD5 hash: {weak_hash}")

    # 🚨 Unsafe base64 operations
      encoded = base64.b64encode(b"malicious_payload").decode()
      decoded = base64.b64decode(encoded)
      print(f"Base64 operations: {encoded} -> {decoded}")

    return "Vulnerable function execute
