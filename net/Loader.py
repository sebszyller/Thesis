import Conf


class Loader:
    def __init__(self, path):
        self.batch_size = Conf.batch_size
        self.epochs = Conf.epochs
        self.layers = Conf.layers
        self.path = path

    def read_file(self):
        with open(self.path) as file_:
            return file_.read().splitlines()

    def print_config(self):
        print "Config:\n batch_size: {0}\n epochs: {1}\n layers: {2}".format(self.batch_size, self.epochs, self.layers)
