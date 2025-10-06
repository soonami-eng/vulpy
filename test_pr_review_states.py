#!/usr/bin/env python3
"""
Test file for PR Review States functionality
This file contains vulnerabilities of different severities to test:
- APPROVE state (no vulnerabilities)
- COMMENT state (medium/low severity)
- REQUEST_CHANGES state (critical/high severity)
"""

import sqlite3
import hashlib
import os
import subprocess
import pickle
import base64
from flask import Flask, request, render_template_string, session, redirect, url_for

app = Flask(__name__)

# CRITICAL: Hardcoded secret key
app.secret_key = "hardcoded_secret_key_12345"

def authenticate_user(username, password):
      """CRITICAL: SQL Injection vulnerability"""
      conn = sqlite3.connect('users.db')
      cursor = conn.cursor()

    # Direct string concatenation - SQL Injection
      query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
      cursor.execute(query)

    user_data = cursor.fetchone()
    conn.close()
    return user_data

def hash_password(password):
      """HIGH: Weak password hashing (MD5)"""
      return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
      """HIGH: Path Traversal vulnerability"""
      with open(f"/tmp/{filename}", 'r') as f:
                return f.read()

  @app.route('/search')
def search():
      """HIGH: XSS vulnerability"""
      query = request.args.get('q', '')
      template = f"<h1>Search Results for: {query}</h1>"
      return render_template_string(template)

@app.route('/login')
def login():
      """MEDIUM: Missing rate limiting"""
      if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']

        # Insecure session management
                session['admin'] = True
                return redirect(url_for('dashboard'))

      return render_template_string('''
          <form method="POST">
              <input name="username" placeholder="Username">
              <input name="password" type="password" placeholder="Password">
              <button type="submit">Login</button>
          </form>
      ''')

@app.route('/debug')
def debug():
      """HIGH: Information disclosure"""
      return {
          'database_path': '/app/users.db',
          'secret_key': app.secret_key,
          'environment': os.environ,
          'system_info': subprocess.run('uname -a', shell=True, capture_output=True, text=True).stdout
      }

@app.route('/upload', methods=['POST'])
def upload_file():
      """HIGH: Insecure file upload"""
      file = request.files['file']
      file.save(f"/uploads/{file.filename}")
      return "File uploaded succe
