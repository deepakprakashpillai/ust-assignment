class ShoppingList:
    def __init__(self):
        self.items = []
        self.index = 0  

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def __iter__(self):
        self.index = 0 
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration 
        
shopping_list = ShoppingList()
shopping_list.add_item("Bread")
shopping_list.add_item("Milk")
shopping_list.add_item("Eggs")
shopping_list.add_item("Apples")

for item in shopping_list:
    print(item)