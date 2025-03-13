from database import Database  # Import database handling
import bcrypt
import pyotp


class UserManagement:
    """Handles user registration, login, and authentication using a database."""

    def __init__(self):
        self.db = Database()

    def check_username(self):
        """Validates username availability and format."""
        while True:
            username = input("Create a username (8-16 characters): ").strip().lower()
            if self.db.user_exists(username):
                print("This username already exists. Try another one.")
            elif 8 <= len(username) <= 16:
                return username
            else:
                print("Invalid username. Use 8-16 characters.")

    def check_password(self):
        """Validates password security criteria."""
        while True:
            password = input("Enter a password (8-16 chars, 1 uppercase, 1 digit): ")
            if (
                8 <= len(password) <= 16
                and any(char.isupper() for char in password)
                and any(char.isdigit() for char in password)
            ):
                return password

            print("Invalid password. Ensure it meets all criteria.")

    def register(self):
        """Registers a new user with a selected role."""
        username = self.check_username()
        password = self.check_password()

        while True:
            role = (
                input(
                    "Select a role (M/Meloman, A/Artist, L/Label, S/SysAdmin, C/ContentAdmin): "
                )
                .strip()
                .lower()
            )
            role_map = {
                "m": "Meloman",
                "meloman": "Meloman",
                "a": "Artist",
                "artist": "Artist",
                "l": "Label",
                "label": "Label",
                "s": "System Administrator",
                "sysadmin": "System Administrator",  # FIXED
                "c": "Content Administrator",
                "contentadmin": "Content Administrator",  # FIXED
            }

            if role in role_map:
                role = role_map[role]
                break

            print("Invalid role. Select M/Meloman, A/Artist, L/Label, S/SysAdmin, or C/ContentAdmin.")

        self.db.add_user(username, password, role)
        print(f"Account created! You are registered as a {role}.")

    def login(self, role):
        """Handles user login with password and OTP verification."""
        attempts = 0
        while attempts < 3:
            username = input("Username: ").strip().lower()
            password = input("Password: ")

            user = self.db.get_user(username)
            if user and user[2] == role:  # user[2] is role in the database
                stored_password, otp_secret = user[1], user[3]

                if bcrypt.checkpw(password.encode("utf-8"), stored_password):
                    totp = pyotp.TOTP(otp_secret)
                    print("Your OTP is:", totp.now())
                    entered_pin = input("Enter the verification pin: ")

                    if totp.verify(entered_pin):
                        print(
                            f"Verification successful!\nWelcome, {username.capitalize()} ({role})."
                        )
                        return (
                            username  # Return username for further role-based actions
                        )

                    print("Incorrect OTP.")
                else:
                    print("Wrong password.")
            else:
                print("Username does not exist or role mismatch.")

            attempts += 1
            if attempts >= 3:
                print("You've exceeded the maximum number of login attempts.")
                return None

        return None
