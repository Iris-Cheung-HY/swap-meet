import uuid

class Item:
    def __init__(self, item, id = None)
        self.item = item
        self.id = uuid.uuid4()
    
    def grab_item_id(self, item, id):
        print (f"{item} is  equal id {id}")
