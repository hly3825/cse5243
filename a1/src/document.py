class Document:
    def __init__(self, id, date, title, topics, places, body):
        self.id = id
        self.date = date
        self.title = title
        self.topics = topics
        self.places = places
        self.body = body

    def __str__(self):
        return "{} {}\n{} {}\n{}\n".format(
                self.id, self.date,
                self.topics, self.places,
                self.title)
        #print self.id, self.date
        #print self.topics, self.places
        #print self.title
        #print self.body
        #print
