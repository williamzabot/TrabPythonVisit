
class Visitor:
    def __init__(self):
        self.name = None
        self.document = None

    def __str__(self):
        return f"{self.name}, documento: {self.document}"
