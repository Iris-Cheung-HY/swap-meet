import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = float(condition) 
    
    def get_category(self):
        #return fix class name
        return "Item"
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."


    def condition_description(self):
        descriptions = {
            0: "Heavily used",
            1: "Well-loved",
            2: "Some signs of wear",
            3: "Lightly used",
            4: "Almost mint",
            5: "Mint condition"
        }

        condition_int = round(self.condition)
        if condition_int < 0:
            condition_int = 0
        elif condition_int > 5:
            condition_int = 5

        return descriptions[condition_int]