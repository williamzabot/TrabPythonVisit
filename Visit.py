
class Visit:
    def __init__(self):
        self.professional = None
        self.visitor = None
        self.time = None

    def __str__(self):
        return f"Visitante {self.visitor.name}, horário: {self.time}"
