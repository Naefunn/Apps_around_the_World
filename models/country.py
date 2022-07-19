class Country:

    def __init__(self, name, description, visited = False, id = None):
        self.name = name
        self.description = description
        self.visited = visited
        self.id = id


    def mark_complete(self):
        self.visited = True