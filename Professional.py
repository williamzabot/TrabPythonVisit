
class Professional:
    def __init__(self):
        self.name = None
        self.specialty = None
        self.office = None

    def __str__(self):
        return f"{self.name}, trabalha como {self.specialty}, sala {self.office}"
