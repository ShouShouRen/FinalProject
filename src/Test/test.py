from .file import File


class Test:
    def __init__(self, args: list[str]):
        if len(args) == 0:
            self.all()
        else:
            import json
            data: dict[str, str] = json.loads(args[0])
            if 'case' in data:
                self.test_case = data['case']
            methods_list: list[str] = self.getFunc()
            method_name: str = f'test{self.test_case}'
            if method_name in methods_list:
                getattr(self, method_name)()
            else:
                print("Test Case Not Found")

    def testFile(self) -> None:
        File()

    def testServer(self) -> None:
        print("Test Server")

    def testClient(self) -> None:
        print("Test Client")

    def all(self) -> None:
        print("\nAll Test\n")
        methods_list: list[str] = self.getFunc()
        for method_name in methods_list:
            if method_name.startswith("test"):
                getattr(self, method_name)()

    def getFunc(self) -> list[str]:
        methods_list = [method for method in dir(self) if callable(
            getattr(self, method)) and not method.startswith("__")]
        return methods_list
