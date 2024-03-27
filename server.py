import socket
import threading
import time
import random

SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
PORT = 7000
ADDR = (SERVER, PORT)

LISTENER_LIMIT = 4
active_clients = []  # List of all currently connected users
all_client = {}
now_price = 100
start = False
restart = False
p = ""
a = 30


def count():
    global a, restart, timer
    if start:
        a = a - 1
    print(a)
    if restart:
        a = 30
        restart = False
    if a > 0:
        timer = threading.Timer(1, count)
        timer.start()
    if a == 0:
        finish()


# Function to listen for upcoming messages from a client
def listen_for_messages(client, username):
    global now_price, restart, p
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':

            final_msg = username + '~' + message
            try:
                int(message)
                now_price = max(now_price, int(message))
                p = username
            except:
                print(message)
            send_messages_to_all(final_msg)
            restart = True
            print(f"{username}: {message}")


# Function to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())


# Function to send any new message to all the clients that
# are currently connected to this server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)


# Function to handle client
def client_handler(client):
    global start
    # Server will listen for client message that will
    # Contain the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '' and not start:
            active_clients.append((username, client))
            num = active_clients.index((username, client))
            prompt_message = "SERVER~" + f"{num}@{username}@\n"
            send_messages_to_all(prompt_message)
            time.sleep(0.02)
            print(prompt_message)
            if num != 0:
                for key in all_client:
                    prompt_message = "SERVER~" + f"{all_client[key]}@{key}@\n"
                    send_messages_to_all(prompt_message)
                    time.sleep(0.02)
                    print(prompt_message)
            all_client[username] = num
            if num == 3:
                start = True
                all_item = {
                    'item1.png': 'Item:\n教授拍立得\nStarting Price:\n100',
                    'item2.png': 'Item:\n教授嘉慶君\nStarting Price:\n100',
                    'item3.png': 'Item:\n教授永浴愛河\nStarting Price:\n100',
                    'item4.png': 'Item:\n教授珍貴雲\nStarting Price:\n100',
                }
                item_now = random.choice(['item1.png', 'item2.png', 'item3.png', 'item4.png'])
                mess = "SERVER~" + f"{item_now}&{all_item[item_now]}&\n"
                send_messages_to_all(mess)
                break
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


def finish():
    if now_price == 100:
        final = "SERVER~unsold"
    else:
        final = p + '~#' + str(now_price)
    send_messages_to_all(final)
    print(final)


# Main function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        server.bind(ADDR)
        print(f"Running the server on {ADDR}")
    except:
        print(f"Unable to bind to host {ADDR}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == '__main__':
    timer = threading.Timer(1, count)
    timer.start()
    main()
