import math

#Basic comparison function for testing
def compareObjects(obj1, obj2):
	return abs(obj1.value - obj2.value)

def getEuclideanDistance(obj1, obj2, precision):
	valueArr1 = obj1.values
	valueArr2 = obj2.values
	acc = 0
	for i in range(len(valueArr1)):
		v1 = float(valueArr1[i])
		v2 = float(valueArr2[i])
		acc += (v1 - v2)**2
	return round(math.sqrt(acc), precision)