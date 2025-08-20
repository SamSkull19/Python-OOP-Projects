class Menu:
    def __init__(self):
        self.items = [] # Database of menu items
    
    def add_menu_items(self, item):
        self.items.append(item)
    
    def find_items(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None    

    def remove_item(self, item_name):
        item = self.find_items(item_name)
        
        if item:
            self.items.remove(item)
            print("Items Deleted")

        else:
            print("Item not Found")

    def show_menu_items(self):
        print('**** MENU ****')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
