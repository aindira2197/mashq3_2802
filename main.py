
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

    def run(self):
        print("Running...")


class Dog(Animal):
        def __init__(self, name, rangi):
            super().__init__(name)
            self.rangi = rangi

        def run(self):
            super().run()
            print("Dog is running...")

