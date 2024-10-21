import os
# This might not work on mac for the appropriate user. 
# See for example: https://github.com/kovidgoyal/kitty/issues/6511
import getpass
from pathlib import Path 

foldername = Path().cwd() / "my_temp_python_folder"

# Create a folder
foldername.mkdir(exist_ok=True)

# Change directory to the newly created folder
os.chdir(foldername)

# Get the username and current directory
# Alternative:
# user_name = os.getlogin()
user_name = getpass.getuser()

current_directory = os.getcwd()

# Set a simple variable for the IP address (example value)
ip_address = "192.168.0.1"

# Write the "local address details" file
with open("local_address_details.txt", "w") as file:
    file.write(f"Username: {user_name}\n")
    file.write(f"Current Directory: {current_directory}\n")
    file.write(f"IP Address: {ip_address}\n")

# Write another file
with open("another_file.txt", "w") as file:
    file.write("This is another file in the folder.")

# Print a message to confirm the script execution
print("Folder and files created successfully!")
