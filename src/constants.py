class ConstantsManager(object):
    def __init__(self):
        self.lag = 7
        self.max_iter = 10000
        self.n_features = 15
        self.test_size = 150
        self.n_splits = 5
        self.EXPLORE_MODE = False
        return


constants = ConstantsManager()
