def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) != len(b):
		return -1
	
	res = []
	for i in range(len(a)):
		added = a[i] + b[i]
		res.append(added)
	return res
	pass