from mergeSort import mergeSort
import numpy as np
import time

for n in range(7):
	a = np.random.rand(10**n)
	startTime = time.perf_counter_ns()
	mergeSort(a)
	endTime = time.perf_counter_ns()
	totalTime = endTime - startTime
	print(10**n, " elements sorted in ", totalTime, "ns.")

# Sample result
# 1  elements sorted in  1200 ns.
# 10  elements sorted in  33600 ns.
# 100  elements sorted in  379100 ns.
# 1000  elements sorted in  4715500 ns.
# 10000  elements sorted in  54342200 ns.
# 100000  elements sorted in  660213100 ns.
# 1000000  elements sorted in  7883840400 ns.