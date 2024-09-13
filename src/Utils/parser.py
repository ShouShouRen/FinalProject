class Parser:
    def __init__(self,args: list[str]):
        self.args = args

    def connect_address(self):
        host: str = 'localhost'
        port: str = "50051"
        if len(self.args) == 1:
            import json
            data: dict[str, str] = json.loads(self.args[0])
            if 'host' in data:
                host = data['host']
            if 'port' in data:
                port = data['port']
        return f"{host}:{port}"