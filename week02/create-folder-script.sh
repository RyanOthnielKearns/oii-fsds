#!/bin/bash

# Create a folder

foldername="my_temp_bash_folder"
mkdir "$foldername"

# Change directory to the newly created folder
cd "$foldername"

# Get the username and current directory
user_name=$(whoami)
current_directory=$(pwd)

# Set a simple variable for the IP address (example value)
ip_address="192.168.0.1"

# Write the "local address details" file
echo "Username: $user_name" > local_address_details.txt
echo "Current Directory: $current_directory" >> local_address_details.txt
echo "IP Address: $ip_address" >> local_address_details.txt

# Write another file
echo "This is another file in the folder." > another_file.txt

# Print a message to confirm the script execution
echo "Folder and files created successfully!"
