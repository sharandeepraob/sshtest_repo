import paramiko

# Define SSH connection parameters
hostname = "172.16.208.131"
port = 22  # Default SSH port
username = "kali"
password = "kali"  # You can also use key-based authentication

# Initialize an SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure for production)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote server
    ssh.connect(hostname, port, username, password)

    # Execute a remote command (e.g., "ls" to list files)
    command = "ls"
    stdin, stdout, stderr = ssh.exec_command(command)

    # Read and print the command output
    output = stdout.read().decode()
    print("Command Output:")
    print(output)

except paramiko.AuthenticationException as e:
    print("Authentication failed:", str(e))
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))
except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Close the SSH connection
    ssh.close()
