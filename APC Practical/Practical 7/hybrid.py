class device:
    def power_on(self):
        print("Power on")

class laptop(device):
    def keyboard(self):
        print("Keyboard input")

class tablet(device):
    def touch(self):
        print("Touch input")

class hybrid(laptop, tablet):
    def use(self):
        self.power_on()
        self.keyboard()
        self.touch()

h = hybrid()
h.use()
