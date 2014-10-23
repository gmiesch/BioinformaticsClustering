import sys
from testObjects import *
from clustering import *

def findAnswer(matrix):
	while(len(matrix) > 2):
		printDistanceMatrix(matrix)
		matrix = mergeClusters(matrix)
	printDistanceMatrix(matrix)

#WORKING IMPLEMENTATION
#object1 = DataObject("A", 12)
#object2 = DataObject("B", 17)
#object3 = DataObject("C", 6)
#object4 = DataObject("D", 24)
#objects = [object1, object2, object3, object4]

#object1 = DataObject("A", 3)
#object2 = DataObject("B", 8)
#object3 = DataObject("C", 15)
#object4 = DataObject("D", 11)
#object5 = DataObject("E", 5)
#objects = [object1, object2, object3, object4, object5]



#mt1 = DistanceMeasurement([object1, object2], [object1, object2], 0)
#mt2 = DistanceMeasurement([object2, object3], [object2, object3], 0)
#testMatrix = []
#testMatrix.append(mt1)
#testMatrix.append(mt2)
#printCluster(testMatrix)

da = buildTestDistanceArray('testMatrix.txt')
#for i in range (len(da)):
#	for j in range (len(da[i])):
#		print da[i][j],
#	print ""
test = buildTestDistanceMatrix(da)

#test = buildDistanceMatrix(objects)
#printDistanceMatrix(test)
#test = mergeClusters(test)
#printDistanceMatrix(test)
#test = mergeClusters(test)
#printDistanceMatrix(test)
#test = mergeClusters(test)
#printDistanceMatrix(test)
#test = mergeClusters(test)
#printDistanceMatrix(test)

findAnswer(test)



