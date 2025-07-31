import socket

# Robot connection details (update as needed)
#robotIP = "192.168.56.101"  # Use the IP address for your simulated robot
robotIP = "192.168.168.5"  #IP Address of real robot
PRIMARY_PORT = 30001        # Primary port for robot command reception
SECONDARY_PORT = 30002
REALTIME_PORT = 30003
new_line = "\n"

def send_urscript_command(command: str):
    """
    Sends a URScript command to the robot.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((robotIP, PRIMARY_PORT))
        # Append newline to ensure the command is executed
        command = command + new_line
        s.sendall(command.encode('utf-8'))
        s.close()
        print("Command sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def send_pose_as_command(pose):
    """
    Formats a URScript command using the given pose (list of 6 elements)
    and sends it to the robot.
    """
    # Convert the pose list to a comma-separated string
    new_pose_str = ", ".join(str(val) for val in pose)
    # Construct the URScript command with the new pose
    command = f"movej([{new_pose_str}], a=0.1, v=0.1, t=20)"
    print(f"Sending command: {command}")
    send_urscript_command(command)

if __name__ == "__main__":
    # For testing: send a default pose command if this module is run directly
    default_pose = [0.260, -0.267, 0.686, 1.93, 0.935, 1.87]
    send_pose_as_command(default_pose)
