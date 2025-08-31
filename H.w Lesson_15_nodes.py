class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def set_next(self, next_node):
        self._next = next_node
    
    def get_next(self):
        return self._next
    
    def get_data(self):
        return self._data

head = None
string_input = input(("please enter the string that you want to convert to linked list of nodes "))
for i, node_value in enumerate(string_input):
    if i == 0:
        new_node = Node(node_value)
        head = new_node
    else:
        current = new_node
        new_node = Node(node_value)
        current.set_next(new_node)

current_node_to_print = head
while current_node_to_print != None:
      print(current_node_to_print.get_data(), end = "->")
      current_node_to_print = current_node_to_print.get_next()




