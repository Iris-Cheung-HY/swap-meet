class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item_to_added):
        self.inventory.append(item_to_added)
        return item_to_added
    
    def remove(self,item_to_removed):
        if item_to_removed not in self.inventory:
            return False

        self.inventory.remove(item_to_removed)
        return item_to_removed
        