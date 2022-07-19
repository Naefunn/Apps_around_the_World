class City:

    def __init__(self, name, description, country_id, visited = False, id = None):
        self.name = name
        self.description = description
        self.id = id
        self.visited = visited
        self.country_id = country_id


    def mark_complete(self):
        self.visited = True