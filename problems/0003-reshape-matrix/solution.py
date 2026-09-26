import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	a = np.array(a)
	try:
		reshaped_matrix = a.reshape(new_shape)
	except ValueError:
		return []

	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	return reshaped_matrix