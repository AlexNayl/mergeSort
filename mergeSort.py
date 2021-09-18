import numpy as np
import math



def mergeSort( array ):
	#print(len(array))
	if len(array) > 1:
		dividerCell = len(array) // 2
		leftArray = array[:dividerCell]
		rightArray = array[dividerCell:]
		array = merge(mergeSort(leftArray), mergeSort(rightArray))
	return array

def merge(left, right):
	#creates an empty array
	size = len(left) + len(right)
	array = [0]*size

	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		array[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		array[k] = right[j]
		j += 1
		k += 1

	return array
