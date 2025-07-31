import socket
import json

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
                action = json.loads(data.decode("utf-8"))
                print(f"Received action: {action}")
                # Save the action to the list
                actions.append(action)
            except json.JSONDecodeError:
                print("Received data is not valid JSON:", data)
            
            # Optional: add a break condition or processing logic
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed.")
    
    # Now you can use the 'actions' variable for further processing
    print("All received actions:", actions)

if __name__ == "__main__":
    run_client()
