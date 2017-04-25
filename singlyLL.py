#######################################################################################
#
#	Singly LL
#
#
#
#######################################################################################
class SNode(object):
 
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
 
class SingleList(object):
 
    head = None
    tail = None
 
    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
 
    def append(self, data):
        node = SNode(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node
 
    def removeFirst(self):
        current_node = self.head
        if(self.head.next is not None):
        	self.head = self.head.next

    def search(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                return True
 
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

        return False

l = SingleList()
l.append(21)
l.append(3)
l.append(43)
l.append(100)
l.append(15)
l.show()
l.removeFirst()
l.show()
