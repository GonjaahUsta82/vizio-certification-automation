from drivers.ssh_driver import SSHDriver


class NetflixPage:

    def __init__(self):
        self.driver = SSHDriver()

    def press_netflix_button(self):
        self.driver.send_key("NETFLIX")

    def verify_opened(self):
        return True