import sys
from random import randint


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
 

class Queue(object):
 
    head = None
    tail = None
 
    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
 
    def enqueue(self, data):
        node = SNode(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node
 
    def dequeue(self):
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


#######################################################################################
#
#	Doubly LL
#
#
#
#######################################################################################
class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoubleList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
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
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next

    def removeHead(self):
        current_node = self.head
        # otherwise we have no prev (it's None), head is the next one, and prev becomes None
        self.head = current_node.next
        current_node.next.prev = None

    def removeTail(self):
        current_node = self.tail
        # otherwise we have no prev (it's None), head is the next one, and prev becomes None
        self.tail = current_node.prev
        current_node.prev.next = None
 

    def search(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                return True

            current_node = current_node.next

        return False

#######################################################################################
#
#	FIFO
#
#
#
#######################################################################################
def inFrame(num, source):
	for i in source:
		if(i == num):
			return True
	return False

#-----------------------------------------------------------------------
#
#	Find the index of the element in the current frame to be replaced:
#		Find the max index of 
#
#
#-----------------------------------------------------------------------
def fifo(res, fr):
	fautls = 0
	fill = 0
	index = 0
	currently_inFrame = 0
	q = Queue()
	print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if( (fill == 0) or (q.search(res[index]) == False)):
				# enqueue the item in the frames
				q.enqueue(res[index])
				# increment the count of number of frames filled
				fill += 1
				fautls += 1
		# if max no of frames are filled, pop and replace
		else:
			# check if next item is already in frame
			#if(inFrame(res[index],) == False):
			if(q.search(res[index]) == False):
				#remove 1st item
				q.dequeue()
				#enqueue the next element 
				q.enqueue(res[index])
				fautls += 1
		# increment the index in the frame array
		index += 1

	return fautls

#######################################################################################
#
#	OPT
#
#
#
#######################################################################################
def nextOccur(targetNum, array, start):
	#print "Find ", targetNum, ", starting from: ", start, ", array len: ", len(array)
	#print "Last elem is: ", array[len(array)-1]
	pos = 0;
	for i in range(start,len(array)):
		if(array[i] == targetNum):
			pos = i
			#print "pos ", array[i], " is ", i
			break
	#if found, pos will be other than 0
	return pos

#-----------------------------------------------------------------------
#
#	Find the index of the element in the current frame to be replaced:
#		Find the max index of 
#
#
#-----------------------------------------------------------------------
def indexReplace(res, list,start):
	distance = []
	for i in list:
		distance.append(100000000) # assume that the array will not exceed 100 mil frames
	for i in range(len(list)):
		# find the index of the next occurence of i starting from start
		nextPos = nextOccur(list[i], res, start)
		#if found the next occurence
		if(nextPos > 0):
			distance[i] = nextPos
	#sort the distance array to find the largest value 
	#print "Distance array: ",distance
	max_distance = max(distance)
	max_index = distance.index(max_distance)
	#print "MAx index: ", max_index
	#assume the last item has the largest distance
	retval = max_index
	return max_index

#-----------------------------------------------------------------------
#
#	Find the index of the element in the current frame to be replaced:
#		Find the max index of 
#
#
#-----------------------------------------------------------------------
def opt(res, fr):
	fautls = 0
	fill = 0
	index = 0
	list = []
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if( (fill == 0) or (res[index] not in list)):
				list.append(res[index])
				fill += 1
				fautls += 1
		else:
			if(res[index] not in list):
				#print "Not in FRAME: ", res[index]
				replaceAt = indexReplace(res, list, index)
				#print "NEXT replaced = ", list[replaceAt]
				list[replaceAt] = res[index]
				#print "List array: ", list
				# print "not in list: ", res[index]
				fautls += 1
		index += 1
	return fautls

#######################################################################################
#
#	Rand
#
#
#######################################################################################
def rand(res, fr):
	fautls = 0
	fill = 0
	index = 0
	list = []
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if( (fill == 0) or (res[index] not in list)):
				list.append(res[index])
				fill += 1
				fautls += 1
		else:
			if(res[index] not in list):
				#print "Not in FRAME: ", res[index]
				replaceAt = randint(0,fr-1)
				#print "NEXT replaced = ", list[replaceAt]
				list[replaceAt] = res[index]
				#print "List array: ", list
				# print "not in list: ", res[index]
				fautls += 1
		# increment the index in the frame array
		index += 1
	return fautls

#######################################################################################
#
#	LRU
#
#
#######################################################################################
def LRU(res, fr):
	fautls = 0
	fill = 0
	index = 0
	d = DoubleList()
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			d.append(res[index])
			# increment the index in the frame array
			index += 1
			# increment the count of number of frames filled
			if(d.search(res[index])):
				fill += 1
				fautls += 1
		else:
			# if found in current frames, update the value of MRU
			if(d.search(res[index]) ):
				d.remove(res[index])
				d.append(res[index])
			else:
				d.removeHead()
				d.append(res[index])
				fautls += 1
			
			index += 1
	
	return fautls

#######################################################################################
#
#	MRU
#
#
#######################################################################################
def MRU(res, fr):
	fautls = 0
	fill = 0
	index = 0
	d = DoubleList()
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			d.append(res[index])
			# increment the index in the frame array
			index += 1
			# increment the count of number of frames filled
			if(d.search(res[index])):
				fill += 1
				fautls += 1
		else:
			# if found in current frames, update the value of MRU
			if(d.search(res[index]) ):
				d.remove(res[index])
				d.append(res[index])
			else:
				d.removeTail()
				d.append(res[index])
				fautls += 1
			
			index += 1
	
	return fautls

#######################################################################################
#
#	MFU
#
#
#######################################################################################
def MFU(res, fr):
	fautls = 0
	fill = 0
	index = 0
	list = []
	count = []
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if( (fill == 0) or (res[index] not in list)):
				list.append(res[index])
				count.append(1)
				fill += 1
				fautls += 1
			if (res[index] in list):
				count[list.index(res[index])] += 1
		else:
			# if found in current frames, update the value of MRU
			if(res[index] in list ):
				count[list.index(res[index])] += 1 
			else:
				max_count = max(count)
				pos = count.index(max_count)
				list[pos] = res[index]
				count[pos] = 1
				fautls += 1
		index += 1
	
	return fautls

#######################################################################################
#
#	LFU
#
#
#######################################################################################
def LFU(res, fr):
	fautls = 0
	fill = 0
	index = 0
	list = []
	count = []
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if( (fill == 0) or (res[index] not in list)):
				list.append(res[index])
				count.append(1)
				fill += 1
				fautls += 1
			if (res[index] in list):
				count[list.index(res[index])] += 1
		else:
			# if found in current frames, update the value of MRU
			if(res[index] in list ):
				count[list.index(res[index])] += 1 
			else:
				min_count = min(count)
				pos = count.index(min_count)
				list[pos] = res[index]
				count[pos] = 1
				fautls += 1
		index += 1
	
	return fautls

#######################################################################################
#
#	main method:
#
#
#
#######################################################################################
#print "Argument List: ", str(sys.argv)
filename = str(sys.argv[1])
#print "file name: ", filename
fp = open(filename)
contents = fp.readlines()

string = contents[0]
result = map(int, string.split(' '))

frames = contents[1]
frame_num = map(int, frames.split(' '))

# ans = fifo(result, frame_num[0])
# print "FIFO: ", ans

# ans = opt(result, frame_num[0])
# print "OPT: ", ans

# ans = LRU(result, frame_num[0])
# print "LRU: ", ans

# ans = MRU(result, frame_num[0])
# print "MRU: ", ans

# ans = MFU(result, frame_num[0])
# print "MFU: ", ans

ans = LFU(result, frame_num[0])
print "LFU: ", ans




	