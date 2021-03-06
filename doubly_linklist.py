#######################################################################################
#
#   Doubly LL
#
#
#
#######################################################################################
class DNode(object):
 
    def __init__(self, data,count, prev, next):
        self.data = data
        self.count = count
        self.prev = prev
        self.next = next
 
 
class DoubleList(object):
 
    head = None
    tail = None
 
    # add a new node to the END of the List
    def append(self, data,count):
        new_node = DNode(data, count, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # add 
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    if(current_node.next is not None):
                        current_node.next.prev = current_node.prev
                    else:
                        self.tail = self.tail.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    if(current_node.next is not None):
                        current_node.next.prev = None
                    else:
                        self.tail = self.tail.prev 
                break
            current_node = current_node.next

    def removeCount(self, count):
        current_node = self.head
 
        while current_node is not None:
            if current_node.count == count:
                num = current_node.data
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    if(current_node.next is not None):
                        current_node.next.prev = current_node.prev
                    else:
                        self.tail = self.tail.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    if(current_node.next is not None):
                        current_node.next.prev = None
                    else:
                        self.tail = self.tail.prev 
                break
            current_node = current_node.next

        return num

    def removeHead(self):
        if self.head is not None:
            if self.head.next is not None:
                current_node = self.head
                # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                self.head = current_node.next
                self.head.prev = None
            else:
                self.head = None

    def removeTail(self):
        current_node = self.tail
        # otherwise we have no prev (it's None), head is the next one, and prev becomes None
        self.tail = current_node.prev
        self.tail.next = None
        current_node.prev = None

    def search(self, node_value):
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_value:
                return True
            current_node = current_node.next
        return False

    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
            current_node = current_node.next
        print "*"*50

    def printCount(self):
        cur = self.head
        while cur is not None:
            print cur.data, "[",cur.count, "]","->",
            cur = cur.next
        print "None"

d = DoubleList()
d.append(7,2)
d.append(0,2)
d.append(1,2)
d.printCount()
num = d.removeCount(2)
print "num removed: ", num
d.append(5,2)
num = d.removeCount(2)
print "num removed: ", num