class Node():
    def __init__(self,value):   #to initiate the node; self: which instance of the node is speaking;
        self.value = value
        self.next = None        # null doesn't exist in Python, but its null

first_node = Node(10)           # first node = self, passed with a value of 10
second_node = Node(22)

# print(first_node.value)
# print(first_node.next)

# print(second_node.value)
# print(second_node.next)

# first_node.next = second_node       # this was called "Frankenstein stitching" LOL!!

# print(first_node.value)
# print(first_node.next)

# print(second_node.value)
# print(second_node.next)

class SLL():
    def __init__(self, head):
        self.head = head
    def add_node_back(self,value):
        # how many nodes precede this node?
        # need last node, ==> last_node.next = new
        runner = self.head
        while(runner.next):
            runner = runner.next
        runner.next = Node(value)        # this is the new node
        return self                     # this is not necessary, but it evaluates to the list
    def add_node_front(self, value):
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    def viewList(self):
        runner = self.head
        while(runner):
            print(runner.value)
            runner = runner.next
    def contains(self, value):
        runner = self.head
        while(runner):
            if(runner.value == value):
                return True
            runner = runner.next
        return False


first_sll = SLL(first_node)

first_sll.add_node_back(22)
first_sll.add_node_back(3)
first_sll.add_node_back(48)
first_sll.add_node_back(19)
first_sll.add_node_front(-8)
first_sll.add_node_front("Hi everyone")

first_sll.viewList()
print(first_sll.contains(48))
# print(first_sll.head.next.value)

# print()