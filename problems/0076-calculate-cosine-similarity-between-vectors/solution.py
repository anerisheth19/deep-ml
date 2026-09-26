import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot_product = 0
	for i in range(len(v1)):
		dot_product += v1[i] * v2[i]
		
	l2_norm_v1 = np.sqrt(np.sum(v1*v1))
	l2_norm_v2 = np.sqrt(np.sum(v2*v2))

	result = dot_product/(l2_norm_v1*l2_norm_v2)
	return result
	pass