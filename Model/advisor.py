class Adivsor:
    def __init__(self, props, advisor_name, email, id):
        self.properties = props
        self.name = advisor_name
        self.id = id
        self.pairings = []
        self.quota = 5

