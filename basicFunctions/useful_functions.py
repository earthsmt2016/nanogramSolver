"""
These contain a list of functions which can be useful to a range of programs.
"""

#Prints out the contents of an array.
def printList(array):
	for item in array:
		print(item);
#Prints out the amount of elements residing in an array.
def countAmountElementsInarray(array):
	return len(array);
#Remove duplicates from a given list.
def removeDuplicatesFromList(array):
	return list(set(array));
#Find the largest number from a given array.
def findLargestNumberFromList(array):
	return max(array);
#Print a header message with a given variable.
def printMessageWithHeaderMessage(headerMessage,number):
	print headerMessage+str(number);
#Sum all elements/items which are in the specified array.
def sumOfAllElementsInsideArray(array):
	return sum(array);
#Sort a list of elements contained inside an array.
def alphaSortArray(array):
	return sorted(array);
