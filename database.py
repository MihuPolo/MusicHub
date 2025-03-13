import sqlite3
import bcrypt
import pyotp


class Database:
    """Handles user database operations."""

    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_users_table()

    def create_users_table(self):
        """Creates the users table if it doesn't exist."""
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password BLOB NOT NULL,
            role TEXT NOT NULL,
            otp_secret TEXT NOT NULL
        )
        """
        )
        self.conn.commit()

    def add_user(self, username, password, role):
        """Registers a new user in the database."""
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        otp_secret = pyotp.random_base32()
        self.cursor.execute(
            "INSERT INTO users (username, password, role, otp_secret) VALUES (?, ?, ?, ?)",
            (username, hashed_password, role, otp_secret),
        )
        self.conn.commit()

    def get_user(self, username):
        """Fetches a user from the database."""
        self.cursor.execute(
            "SELECT username, password, role, otp_secret FROM users WHERE username = ?",
            (username,),
        )
        return self.cursor.fetchone()  # Returns (username, password, role, otp_secret)

    def user_exists(self, username):
        """Checks if a username exists in the database."""
        self.cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone() is not None

    def close(self):
        """Closes the database connection."""
        self.conn.close()
