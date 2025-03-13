from file_storage import FileStorage  # Import secure file storage

class RoleBasedActions:
    """Handles actions based on user roles."""

    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.file_storage = FileStorage()  # Initialize file storage system

    def execute_role_actions(self):from file_storage import FileStorage

class RoleBasedActions:
    """Handles actions based on user roles."""

    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.file_storage = FileStorage()

    def execute_role_actions(self):
        """Directs user to appropriate role-based actions."""
        role_actions = {
            "Meloman": self.meloman_actions,
            "Artist": self.artist_actions,
            "Label": self.label_actions,
            "System Administrator": self.sysadmin_actions,
            "Content Administrator": self.content_admin_actions,
        }
        action = role_actions.get(self.role)
        if action:
            action()
        else:
            print("Invalid role!")

    def artist_actions(self):
        while True:
            print("\n Artist Dashboard")
            print("1. Upload File")
            print("2. Retrieve File")
            print("3. List My Files")
            print("4. Exit")
            choice = input("Choose an action: ").strip()

            if choice == "1":
                file_path = input("Enter the path of the file to upload: ").strip()
                self.file_storage.store_file(self.username, file_path)

            elif choice == "2":
                file_name = input("Enter the name of the file to retrieve: ").strip()
                self.file_storage.retrieve_file(self.username, file_name)

            elif choice == "3":
                self.file_storage.list_artist_files(self.username)

            elif choice == "4":
                break

            else:
                print("Invalid choice. Try again.")

        """Directs user to appropriate role-based actions."""
        role_actions = {
            "Meloman": self.meloman_actions,
            "Artist": self.artist_actions,
            "Label": self.label_actions,
            "System Administrator": self.sysadmin_actions,
            "Content Administrator": self.content_admin_actions,
        }
        action = role_actions.get(self.role)
        if action:
            action()
        else:
            print("Invalid role!")

    def meloman_actions(self):
        print("\n Meloman (Listener) Dashboard")
        print("1. Manage Profile")
        print("2. Follow Artists and Labels")
        print("3. Browse Content")
        print("4. Create and Manage Playlists")
        print("5. View Listening History")
        print("6. Save Favorite Songs")
        input("Choose an action: ")

    def artist_actions(self):
        while True:
            print("\n Artist Dashboard")
            print("1. Upload File (Lyrics/Scores)")
            print("2. Retrieve File")
            print("3. List My Files")
            print("4. Exit")
            choice = input("Choose an action: ").strip()

            if choice == "1":
                file_path = input("Enter the path of the file to upload: ").strip()
                self.file_storage.store_file(self.username, file_path)

            elif choice == "2":
                file_name = input("Enter the name of the file to retrieve: ").strip()
                self.file_storage.retrieve_file(self.username, file_name)

            elif choice == "3":
                self.file_storage.list_artist_files(self.username)

            elif choice == "4":
                break

            else:
                print("Invalid choice. Try again.")

    def label_actions(self):
        print("\n Label Dashboard")
        print("1. Update Biography")
        print("2. Manage Artists")
        print("3. Track Artist Performance")
        input("Choose an action: ")

    def sysadmin_actions(self):
        print("\n System Administrator Dashboard")
        print("1. Manage User Accounts")
        print("2. Monitor System Security")
        print("3. View System Logs")
        input("Choose an action: ")

    def content_admin_actions(self):
        print("\n Content Administrator Dashboard")
        print("1. Approve/Reject Content")
        print("2. Handle Copyright Issues")
        print("3. Ensure Metadata Correctness")
        input("Choose an action: ")
