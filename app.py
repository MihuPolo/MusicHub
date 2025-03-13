from user_management import UserManagement
from role_actions import RoleBasedActions

class App:
    """Main application to manage user interactions."""

    def __init__(self):
        self.user_management = UserManagement()

    def run(self):
        print("Welcome to MusicHub")
        while True:
            acc_que = input("Do you have a user account? (Type [YES] or [NO]): ").strip().lower()

            if acc_que == 'no':
                self.user_management.register()
                continue

            elif acc_que == 'yes':
                role_input = input("Which type of account are you logging into? (M/Meloman, A/Artist, L/Label, S/SysAdmin, C/ContentAdmin): ").strip().lower()
                roles = {
                    "m": "Meloman", "a": "Artist", "l": "Label",
                    "s": "System Administrator", "c": "Content Administrator"
                }

                if role_input in roles:
                    role = roles[role_input]
                    username = self.user_management.login(role)
                    if username:
                        RoleBasedActions(username, role).execute_role_actions()
                else:
                    print("Invalid role. Please try again.")

if __name__ == "__main__":
    app = App()
    app.run()
