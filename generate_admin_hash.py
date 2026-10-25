from getpass import getpass
from werkzeug.security import generate_password_hash

password = getpass("Enter the admin password to hash: ")
if len(password) < 12:
    raise SystemExit("Use an admin password with at least 12 characters.")
print(generate_password_hash(password))
