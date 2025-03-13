import os
import hashlib
import sqlite3
import time
from cryptography.fernet import Fernet

# Generate a secure encryption key (Save this in a secure place!)
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

class FileStorage:
    """Handles secure storage, retrieval, and encryption of artist files."""

    def __init__(self, db_name="files.db", storage_dir="stored_files"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
        self.create_files_table()

    def create_files_table(self):
        """Creates the files metadata table if it doesn't exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_username TEXT NOT NULL,
            file_name TEXT NOT NULL,
            encrypted_file_path TEXT NOT NULL,
            checksum TEXT NOT NULL,
            created_at TEXT NOT NULL,
            modified_at TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def calculate_checksum(self, file_path):
        """Generates a SHA-256 checksum for a given file."""
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()

    def encrypt_file(self, file_path):
        """Encrypts the file and returns the encrypted data."""
        with open(file_path, "rb") as file:
            encrypted_data = cipher.encrypt(file.read())
        return encrypted_data

    def decrypt_file(self, encrypted_data):
        """Decrypts encrypted file data."""
        return cipher.decrypt(encrypted_data)

    def store_file(self, artist_username, original_file_path):
        """Encrypts, stores, and records file metadata."""
        if not os.path.exists(original_file_path):
            print("Error: File not found.")
            return

        file_name = os.path.basename(original_file_path)
        encrypted_file_path = os.path.join(self.storage_dir, f"{file_name}.enc")

        # Encrypt file and store it
        encrypted_data = self.encrypt_file(original_file_path)
        with open(encrypted_file_path, "wb") as f:
            f.write(encrypted_data)

        # Compute checksum and timestamps
        checksum = self.calculate_checksum(original_file_path)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Store metadata in database
        self.cursor.execute("""
            INSERT INTO files (artist_username, file_name, encrypted_file_path, checksum, created_at, modified_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (artist_username, file_name, encrypted_file_path, checksum, timestamp, timestamp))
        self.conn.commit()

        print(f" File '{file_name}' securely stored for {artist_username}.")

    def retrieve_file(self, artist_username, file_name):
        """Decrypts and retrieves a file for an artist."""
        self.cursor.execute("""
            SELECT encrypted_file_path FROM files WHERE artist_username = ? AND file_name = ?
        """, (artist_username, file_name))
        result = self.cursor.fetchone()

        if result:
            encrypted_file_path = result[0]
            with open(encrypted_file_path, "rb") as f:
                encrypted_data = f.read()

            decrypted_data = self.decrypt_file(encrypted_data)
            output_path = os.path.join("retrieved_files", file_name)
            os.makedirs("retrieved_files", exist_ok=True)

            with open(output_path, "wb") as f:
                f.write(decrypted_data)

            print(f" File '{file_name}' successfully retrieved at '{output_path}'.")
            return output_path
        else:
            print(" File not found.")
            return None

    def list_artist_files(self, artist_username):
        """Lists all files uploaded by an artist."""
        self.cursor.execute("""
            SELECT file_name, created_at, modified_at FROM files WHERE artist_username = ?
        """, (artist_username,))
        files = self.cursor.fetchall()

        if files:
            print(f"\n Files for {artist_username}:")
            for file in files:
                print(f"- {file[0]} (Created: {file[1]}, Modified: {file[2]})")
        else:
            print(" No files found.")

    def close(self):
        """Closes the database connection."""
        self.conn.close()
