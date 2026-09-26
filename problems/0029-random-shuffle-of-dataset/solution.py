import numpy as np

def shuffle_data(X, y, seed=None):

	rng = np.random.seed(seed)
	indices = np.random.permutation(len(X))

	return X[indices], y[indices]
	# Your code here
	pass