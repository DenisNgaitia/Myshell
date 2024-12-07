import os
import subprocess

def simple_shell():
    while True:
        # Display a prompt
        command = input("Hello Denis:) ")

        # Exit the shell if the user types 'exit'
        if command.lower() in ['exit', 'quit']:
            print("Exiting shell.")
            break

        # Execute the command
        try:
            # Split the command into a list
            args = command.split()
            # Use subprocess to execute the command
            result = subprocess.run(args, check=True)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_shell()

