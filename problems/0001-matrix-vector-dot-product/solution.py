def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	# if len(a[0]) != len(b):
	# 	return -1

	# dot_product = []
	# for row in a:
	# 	res = 0
	# 	for i in range(len(row)):
	# 		res += row[i] * b[i]
	# 	dot_product.append(res)
	
	# return dot_product

	import numpy as np
	
	if len(a[0]) != len(b):
		return -1
	
	dot_product = []
	for row in a:
		res = 0
		res = np.dot(row, b)
		dot_product.append(res)

	return dot_product	
	pass