from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from auction import Ui_Form
import socket
import threading
import time

PORT = 7000
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
all_client = {}
now_price = 0
start = False
restart = False
a = 30


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Control(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAttr()
        self.initFun()
        self.timer = QtCore.QTimer()  # 加入定時器
        self.timer.timeout.connect(self.count)  # 設定定時要執行的 function
        self.timer.start(1000)  # 啟用定時器，設定間隔時間為 1000 毫秒

    def initAttr(self):
        self.setWindowTitle("Auction")

    def initFun(self):
        self.getin.clicked.connect(self.into_auc)
        self.bid.clicked.connect(self.bidding)

    def count(self):
        global a, restart
        if start:
            a = a - 1
            self.time_left.setText(str(a))
            # print(a)
        if restart:
            a = 30
            self.time_left.setText(str(a))
            restart = False
        if a <= 0:
            self.time_left.setText("0")

    def into_auc(self):
        username = self.yourname.text()
        if username == '':
            QMessageBox.information(None, 'Error', 'Username cannot be empty')
            return
        try:
            # Connect to the server
            client.connect(ADDR)
            print("Successfully connected to server")
        except:
            QMessageBox.information(None, 'Error', 'Unable to connect to server')

        client.sendall(username.encode())
        self.start.setVisible(False)
        self.yourname.setVisible(False)
        self.getin.setVisible(False)

        threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()

    def bidding(self):
        if not start:
            QMessageBox.information(None, 'Error', 'Please wait for other participants')
            self.lineEdit.setText("")
            return
        p = self.lineEdit.text()
        try:
            int(p)
        except:
            QMessageBox.information(None, 'Error', 'Please enter an integer')
            self.lineEdit.setText("")
            return
        if int(p) <= now_price:
            QMessageBox.information(None, 'Error', 'Please bid higher than the price now')
            self.lineEdit.setText("")
            return
        send_message(p)


def listen_for_messages_from_server(client):
    global now_price, a, restart
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split('~')[1]

            # 最後結果
            if content.count("#"):
                text = "Buyer:\n" + username + "\nHammer Price:\n" + str(now_price)
                Form.host.setText(text)
                time.sleep(8)
                Form.start.setPixmap(QtGui.QPixmap("finish.png"))
                Form.start.setVisible(True)
                break
            if content == "unsold":
                Form.host.setText("Unsold")
                time.sleep(8)
                Form.start.setPixmap(QtGui.QPixmap("finish.png"))
                Form.start.setVisible(True)
                break

            # 顯示client
            if content.count("@"):
                show_name(content)
                print(message)

                if message.count("\n") > 1:
                    content = message.split('~')[2]
                    print('3 ' + content)
                    show_name(content)

                if message.count("\n") > 2:
                    content = message.split('~')[3]
                    print('5 ' + content)
                    show_name(content)
                continue

            if content.count('&'):
                item_now = content.split('&')[0]
                item_des = content.split('&')[1]
                start_auction(item_now, item_des)
                continue

            print(content)
            try:
                now_price = max(now_price, int(content))
                Form.host.setText(f"Price:\n{now_price}")
                restart = True
            except:
                return

            # print(message)
            print(all_client[username])

            # 顯示出價
            if all_client[username] == '0':
                Form.price1.setVisible(True)
                Form.price1.setText(f"{content}")
                time.sleep(3)
                Form.price1.setVisible(False)
            elif all_client[username] == '1':
                Form.price2.setVisible(True)
                Form.price2.setText(f"{content}")
                time.sleep(3)
                Form.price2.setVisible(False)
            elif all_client[username] == '2':
                Form.price3.setVisible(True)
                Form.price3.setText(f"{content}")
                time.sleep(3)
                Form.price3.setVisible(False)
            elif all_client[username] == '3':
                Form.price4.setVisible(True)
                Form.price4.setText(f"{content}")
                time.sleep(3)
                Form.price4.setVisible(False)


def send_message(message):
    if message != '':
        client.sendall(message.encode())
        Form.lineEdit.setText("")
    else:
        QMessageBox.information(None, 'Error', 'Please enter the price')


def start_auction(item_now, item_des):
    global start
    Form.host.setText(str(item_des))
    Form.item.setPixmap(QtGui.QPixmap(item_now))
    Form.item.setVisible(True)
    start = True
    return


def show_name(content):
    if content.find('@') != -1:
        user_number = content.split('@')[0]
        name = content.split('@')[1]
        # print('message ' + message)
        print('content ' + content)
        print(all_client)
        all_client[name] = user_number
        if int(user_number) == 0:
            Form.name1.setText(name)
            Form.pic1.setPixmap(QtGui.QPixmap("on.png"))
            if name == Form.yourname.text():
                Form.pic1.setPixmap(QtGui.QPixmap("you.png"))
        elif int(user_number) == 1:
            Form.name2.setText(name)
            Form.pic2.setPixmap(QtGui.QPixmap("on.png"))
            if name == Form.yourname.text():
                Form.pic2.setPixmap(QtGui.QPixmap("you.png"))
        elif int(user_number) == 2:
            Form.name3.setText(name)
            Form.pic3.setPixmap(QtGui.QPixmap("on.png"))
            if name == Form.yourname.text():
                Form.pic3.setPixmap(QtGui.QPixmap("you.png"))
        elif int(user_number) == 3:
            Form.name4.setText(name)
            Form.pic4.setPixmap(QtGui.QPixmap("on.png"))
            if name == Form.yourname.text():
                Form.pic4.setPixmap(QtGui.QPixmap("you.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Control()
    Form.show()
    sys.exit(app.exec_())
