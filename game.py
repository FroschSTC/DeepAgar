from threading import Thread


class Game(Thread):

    def __init__(self):
        pass

    def begin(self, async=False):
        if async:
            self.start()
        else:
            self.run()


if __name__ == "__main__":
    g = Game()
    g.start()