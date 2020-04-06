from page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()#不要传参

    def test_register(self):
        self.main.goto_register().register()#链式调用
