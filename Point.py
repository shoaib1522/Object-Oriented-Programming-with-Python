class Point(object):
    def __init__(self, Location):
        self.location = Location

    def __str__(self):
        return " , Location: {} ".format(self.location)