from .item import Item

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

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or \
        len(other_vendor.inventory) == 0:
            return False
        else:
            my_swap = self.inventory[0]
            friend_swap = other_vendor.inventory[0]
            
            self.inventory[0] = friend_swap
            other_vendor.inventory[0] = my_swap

            if self.inventory[0] == friend_swap and \
            other_vendor.inventory[0] == my_swap:
                return True