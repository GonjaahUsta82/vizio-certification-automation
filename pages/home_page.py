from drivers.ssh_driver import SSHDriver


class HomePage:

    def __init__(self):
        self.driver = SSHDriver()

    def press_home(self):
        self.driver.send_key("HOME")