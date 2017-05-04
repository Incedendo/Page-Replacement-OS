import sys
from random import randint
from singlyLL import SNode, Queue
from doubly_linklist import DNode, DoubleList
from importFile import printMess as simpager_printMess

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
	q = Queue()
	for num in res:
		if(fill < fr):
			if(q.search(num) == False):
				# enqueue the item in the frames
				q.enqueue(num)
				# increment the count of number of frames filled
				fill += 1
				fautls += 1
		# if max no of frames are filled, pop and replace
		else:
			if(q.search(num) == False):
				#remove 1st item
				q.dequeue()
				#enqueue the next element 
				q.enqueue(num)
				fautls += 1

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
	# 
	d = DoubleList()
	#print "frame num: ", fr
	for num in res:
		if(fill < fr):
			# if the frame already resided in the list
			# take the frame out and update the position to the top of the stack
			# keep the fill var the same
			if(d.search(num)):
				d.remove(num)
				d.append(num, 0)
			# if the frame IS NEW
			else: 
				d.append(num, 0)
				fill += 1
				fautls += 1
		else:
			# if found in current frames, 
			if(d.search(num)):
				d.remove(num)
				d.append(num, 0)
			else:
				# remove the very first frame added ( least recently used)
				d.removeHead()
				d.append(num, 0)
				fautls += 1			

	return fautls

#######################################################################################
#
#	MRU
#		
#
#
#######################################################################################
def MRU(res, fr):
	fautls = 0
	fill = 0
	index = 0
	d = DoubleList()
	#print "frame num: ", fr
	for num in res:
		if(fill < fr):
			if(d.search(num) ):
				d.remove(num)
				d.append(num,0)
			else:
				d.append(num, 0)
				fill += 1 		# increment the count of number of frames filled
				fautls += 1
		else:
			# if found in current frames, update the value of MRU
			if(d.search(num) ):
				d.remove(num)
				d.append(num,0)
			else:
				d.removeTail()
				d.append(num,0)
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
	faults = 0
	fill = 0
	index = 0
	list = []
	count = []
	#print "frame num: ", fr
	for i in res:
		if(fill < fr):
			if (res[index] in list):
				count[list.index(res[index])] += 1
				#print "count of " + str(res[index]) + " = " + str(count[list.index(res[index])])
			if( res[index] not in list ):
				list.append(res[index])
				count.append(1)
				#print "count of " + str(res[index]) + " = " + str(count[list.index(res[index])])
				fill += 1
				faults += 1
		else:
			# if found in current frames, update the value of MRU
			if(res[index] in list ):
				count[list.index(res[index])] += 1 
				#print "count of " + str(res[index]) + " = " + str(count[list.index(res[index])])
			else:
				max_count = max(count)
				# find the index of the MFU frame in the list
				pos = count.index(max_count)
				print "Replacing " + str(list[pos]) + " with " + str(res[index])
				# replace the MFU frame with the newly referenced frame
				list[pos] = res[index]
				# update the count of the newly referenced frame.
				count[pos] = 1
				#print "count of " + str(list[pos]) +" = " + str(count[pos])
				faults += 1
		index += 1
		print "fault = " + str(faults) + " , list: "+ str(list) +", count: " + str(count) 
		# print count
	
	return faults

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
	d = DoubleList()
	for num in res:
		# only for the first fr frame
		if(fill < fr):
			# case when that frame has been added previously and there are still available frame
			if (num in list):
				count[list.index(num)] += 1
				d.remove(num)
				d.append(num, count[list.index(num)])
				# print "index = " + str(list.index(num))
			# 1st frame or if that frame haven't been added yet
			if( num not in list ):
				d.append(num, 1)  # add to the queue at the same time
				list.append(num)
				count.append(1)
				fill += 1
				fautls += 1
		else:
			# if found in current frames, update the value of MRU
			if(num in list ):
				count[list.index(num)] += 1 
				# update position of the frame in the QUEUE
				d.remove(num)
				d.append(num, count[list.index(num)])
				d.printCount()
			else:
				min_count = min(count)
				numReplaced = d.removeCount(min_count)
				print "Num replaced = ", numReplaced
				pos = list.index(numReplaced)
				list[pos] = num
				count[pos] = 1
				fautls += 1
				d.append(num,1)  # add to the queue at the same time
				d.printCount()
		print list
	
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

# ans = rand(result, frame_num[0])
# print "Rand: ", ans

# ans = LRU(result, frame_num[0])
# print "LRU: ", ans

# ans = MRU(result, frame_num[0])
# print "MRU: ", ans

# ans = MFU(result, frame_num[0])
# print "MFU: ", ans

ans = LFU(result, frame_num[0])
print "LFU: ", ans

# simpager_printMess(filename)




	