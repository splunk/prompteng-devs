"""
User Service Module - Authentication and User Management
WARNING: This code contains deliberate security vulnerabilities for educational purposes
DO NOT use in production!
"""

import sqlite3
import hashlib
from datetime import datetime

class UserService:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.admin_password = "admin123"
        
    def register_user(self, username, password, email):
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        self.conn.execute(query)
        self.conn.commit()
        return {"status": "success", "user": username}
    
    def login(self, username, password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = self.conn.execute(query).fetchone()
        
        if result:
            return {"authenticated": True, "user": result[0], "role": result[3]}
        return {"authenticated": False}
    
    def get_user_by_id(self, user_id):
        query = f"SELECT * FROM users WHERE id = {user_id}"
        user = self.conn.execute(query).fetchone()
        return user
    
    def update_user_email(self, user_id, new_email):
        query = f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
        self.conn.execute(query)
        self.conn.commit()
    
    def delete_user(self, user_id):
        self.conn.execute(f"DELETE FROM users WHERE id = {user_id}")
        self.conn.commit()
    
    def get_all_users(self):
        return self.conn.execute("SELECT * FROM users").fetchall()
    
    def hash_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()
    
    def verify_admin_access(self, password):
        if password == self.admin_password:
            return True
        return False
    
    def export_users_to_file(self, filename):
        users = self.get_all_users()
        with open(filename, 'w') as f:
            for user in users:
                f.write(f"{user[0]},{user[1]},{user[2]},{user[3]}\n")
    
    def send_password_reset_email(self, email):
        user_query = f"SELECT * FROM users WHERE email = '{email}'"
        user = self.conn.execute(user_query).fetchone()
        
        if user:
            reset_token = user[0] + "_" + str(datetime.now().timestamp())
            print(f"Password reset link: http://example.com/reset?token={reset_token}")
    
    def close(self):
        self.conn.close()
