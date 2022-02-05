import os


class PathManager(object):
    def __init__(self):
        # Application paths
        self.albus_root = os.path.dirname(os.path.abspath(__file__))
        self.data = os.path.join(self.albus_root, 'data')
        self.eight_hr_data = os.path.join(self.data, 'eighthr.data')
        self.names = os.path.join(self.data, 'eighthr.names')
        self.columns = os.path.join(self.data, 'eighthr_columns.txt')
        return


path_manager = PathManager()
