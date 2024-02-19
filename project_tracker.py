import os

# Function to check memory

def check_memory():
    memory_status = os.popen('free -m').read()
    return memory_status

# Function to read a file

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

# Function to write to a file

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
