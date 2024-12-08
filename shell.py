import os
import subprocess
import readline  # Import readline for command history

def simple_shell():
    while True:
        # Display a prompt
        command = input("Hello Denis:) ")

        # Exit the shell if the user types 'exit'
        if command.lower() in ['exit', 'quit']:
            print("Exiting shell.")
            break

        # Add the command to history
        readline.add_history(command)

        # Execute the command
        try:
            # Check for pipes in the command
            if '|' in command:
                commands = [cmd.strip() for cmd in command.split('|')]
                processes = []

                for cmd in commands:
                    # Split the command into a list
                    args = cmd.split()
                    # Create a subprocess for each command
                    if processes:
                        # Use the output of the previous command as the input for the next
                        process = subprocess.Popen(args, stdin=processes[-1].stdout, stdout=subprocess.PIPE)
                    else:
                        process = subprocess.Popen(args, stdout=subprocess.PIPE)
                    processes.append(process)

                # Wait for the last process to complete
                output, _ = processes[-1].communicate()
                print(output.decode())  # Print the final output

            else:
                # Split the command into a list for single commands
                args = command.split()
                # Use subprocess to execute the command
                result = subprocess.run(args, check=True)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_shell()

