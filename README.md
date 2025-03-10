### MusicHub
MusicHub
MusicHub: Secure User & File Management System

Overview

MusicHub is a secure role-based user management system that allows different user types (Meloman, Artist, Label, System Administrator, Content Administrator) to interact with the platform.

Artists can securely upload, store, and retrieve files (lyrics, scores, etc.) with encryption & checksum verification.

Role-based access control allows different user types to perform specific actions.

Secure authentication includes hashed passwords and OTP verification.

Features
User Registration & Login (with OTP authentication)

Role-Based Actions

Secure File Storage (Artists can upload & retrieve encrypted files)

Automatic Checksum Calculation

Timestamps for File Modifications

Encrypted Data Storage (using cryptography library)

Persistent Storage using SQLite Databases

Install dependencies:
bcrypt: Secure password hashing to protect user credentials.

pyotp: One-Time Password (OTP) generation for two-factor authentication.

cryptography: Secure encryption for file storage.

sqlite3: Lightweight database to store user and file metadata.

Usage Guide
Start the application:
python app.py

Register or log in as a user.

Select a role and perform actions:

Meloman: Manage playlists and follow artists.

Artist: Upload, retrieve, and list encrypted files.

Label: Manage artist collaborations.

System Admin: Manage users and system security.

Content Admin: Moderate uploaded content.

Artists can securely upload and retrieve encrypted files:
Upload a file by entering its path.

Retrieve a file by specifying its name.

Check file integrity using automatic checksum validation.

Security Measures
Password Protection: Hashed using bcrypt to prevent leaks.

Two-Factor Authentication: Implemented with pyotp for OTP verification.

File Encryption: cryptography.fernet ensures secure storage.

Checksum Validation: SHA-256 hash verification for file integrity.

Database Storage: Uses SQLite (sqlite3) for storing user credentials and file metadata.

References
Dworkin, M. J. (2015) 'SHA-256 Secure Hash Standard', National Institute of Standards and Technology, Available at: https://nvlpubs.nist.gov

Provos, N. and Mazieres, D. (1999) 'Bcrypt: A Secure Password Hashing Algorithm', USENIX Conference on Security Symposium.

Tollefsen, M. (2017) 'An Introduction to OTP Authentication', Journal of Cyber Security, 14(3), pp. 15-28.

Ferguson, N. and Schneier, B. (2003) Practical Cryptography. New York: Wiley.

SQLite (2023) 'SQLite Database Documentation', Available at: https://www.sqlite.org/docs.html
