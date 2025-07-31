import socket

# initialize variables
#ALL IS DONE IN BASE FRAME
#robotIP = "192.168.168.5" #192.168.56.101 for sim 192.168.168.5 for robot
robotIP = "192.168.56.101"
PRIMARY_PORT = 30001
SECONDARY_PORT = 30002
REALTIME_PORT = 30003

pose = [0.260, -0.267, 0.686, 1.93, 0.935, 1.87]
# URScript command being sent to the robot
urscript_command = urscript_command = "movej([0.260, -0.267, 0.686, 1.93, 0.935, 1.87], a=0.1, v=0.1, t=20)"
#movel([x_pos,y_pos,z_pos,x_rot,y_rot,z_rot]) THIS IS FOR THE END EFFECTOR POSITION
# Creates new line
new_line = "\n"

def send_urscript_command(command: str):
    """
    This function takes the URScript command defined above, 
    connects to the robot server, and sends 
    the command to the specified port to be executed by the robot.

    Args:
        command (str): URScript command
        
    Returns: 
        None
    """
    try:
        # Create a socket connection with the robot IP and port number defined above
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((robotIP, PRIMARY_PORT))

        # Appends new line to the URScript command (the command will not execute without this)
        command = command+new_line
        
        # Send the command
        s.sendall(command.encode('utf-8'))
        
        # Close the connection
        s.close()

    except Exception as e:
        print(f"An error occurred: {e}")

send_urscript_command(urscript_command)