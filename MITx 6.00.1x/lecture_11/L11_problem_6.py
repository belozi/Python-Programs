
class Queue(object):

    def __init__(self):
        self.line = []

    def insert(self, e):
        self.line.append(e)

    def remove(self):
        if self.line == []:
            raise ValueError()
        else:
            e = self.line[0]
            self.line.remove(e)
            return e

queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()


