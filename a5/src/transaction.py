class transaction:

    def __init__(self, id, labels, features):
        self.id = id
        self.labels = labels
        self.features = features

    def __repr__(self):
        return "txn_id: {}, features: {}, labels: {}".format(self.id, self.labels, self.features)