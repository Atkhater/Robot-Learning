import socket
import json
import math
from ur_rcv_sim import send_pose_as_command  # Function to send URScript command

def set_initial_pose():
    # Define initial pose in degrees
    initial_pose_deg = [-91.71, -98.96, -126.22, -46.29, 91.39, -1.78]
    # Convert degrees to radians (URScript often expects radians)
    initial_pose_rad = [d * math.pi / 180 for d in initial_pose_deg]
    # Send the initial pose command
    send_pose_as_command(initial_pose_deg)
    print("Initial pose set.")

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Replace with your server's actual IP address
    server_ip = "192.168.168.42"  
    server_port = 8000
    actions = []  # List to store received actions

    try:
        client.connect((server_ip, server_port))
        print(f"Connected to server at {server_ip}:{server_port}")

        while True:
            data = client.recv(1024)
            if not data:
                print("No data received. Closing connection.")
                break

            try:
                # The received data is expected to be a list of dictionaries
                action_list = json.loads(data.decode("utf-8"))
                print(f"Received action: {action_list}")
                actions.append(action_list)
                
                # Process only the first action in the list
                if isinstance(action_list, list) and len(action_list) > 0:
                    first_action = action_list[0]
                    # Extract the first 6 elements from 'pos_end_effector'
                    pose = first_action.get("pos_end_effector", [])[:6]
                    if len(pose) == 6:
                        send_pose_as_command(pose)
                    else:
                        print("Received pose does not contain 6 elements:", pose)
                else:
                    print("Action is not in expected format:", action_list)
            except json.JSONDecodeError:
                print("Received data is not valid JSON:", data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed.")
    
    print("All received actions:", actions)

if __name__ == "__main__":
    # Set the initial pose before starting the simulation client
    #set_initial_pose()
    run_client()
