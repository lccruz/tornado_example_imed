from websocket import create_connection


def client():
    url = "ws://127.0.0.1:8888/websocket/"
    ws = create_connection(url)
    while True:
        command = input("Digite (r) para recive ou (s) para send: ")
        if command == 'r':
            message = ws.recv()
            print(message)
        elif command == 's':
            message = input("Digite a mensagem: ")
            ws.send(message)
        else:
            ws.close()
            break

if __name__ == "__main__":
    client()
