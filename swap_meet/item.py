import uuid

class Item:
    def __init__(self, id = None):
        self.id = id
        if id == None:
            self.id = uuid.uuid4().int
    
    def get_category(self):
        return "Item"
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
