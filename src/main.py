from Server.server import server
from Client.client import client
from Test import Test
import signal


class Main:
    def __init__(self, args: list[str]):
        if len(args) < 2:
            self.help()
            sys.exit(1)
        match args[1]:
            case 'server':
                self.service = server
            case 'client':
                self.service = client
            case 'test':
                self.service = Test
            case _:
                self.help()
                sys.exit(1)
        self.args = args[2:]
        self.service(self.args)

    def help(self):
        print('''Usage: ./execute [server|client|test] [args]\n\n使用json格式的參數: {"host":"","port":""}\n''')


def signal_handler(signal, frame):
    print("\nShutting Down.")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    import sys
    app = Main(sys.argv)
