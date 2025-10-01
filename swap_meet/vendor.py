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
            

    def get_by_category(self, category = ""):
        category_list = []
        for item in self.inventory:
            if category == item.get_category():
                category_list.append(item)
        return category_list
    
    def get_best_by_category(self, category = ""):
        highest_condition = 0.0
        highest_condition_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_condition_item = item
        return highest_condition_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        ven_best_item = self.get_best_by_category(category = their_priority)
        other_ven_best_item = other_vendor.get_best_by_category(category = my_priority)
        if ven_best_item is None or other_ven_best_item is None:
            return False

        
        if ven_best_item.get_category() != their_priority or \
        other_ven_best_item.get_category() != my_priority:
            return False
        else:
            for item in self.inventory:
                if item == ven_best_item:
                    self.inventory.remove(item)
            self.inventory.append(other_ven_best_item)

            for other_ven_item in other_vendor.inventory:
                if other_ven_item == other_ven_best_item:
                    other_vendor.inventory.remove(other_ven_item)
            other_vendor.inventory.append(ven_best_item)
            
            return True

