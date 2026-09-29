import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	res = {}
	magnitude = 0
	for val in gradient:
		magnitude += val * val
	magnitude = np.sqrt(magnitude)

	if magnitude == 0:
		direction = [0 for val in gradient]
		descent_direction = [0 for val in gradient]
	else:	
		direction = []
		for val in gradient:
			direction.append(val/magnitude)
		
		descent_direction = []
		for val in direction:
			descent_direction.append(-val)

	res['magnitude'] = magnitude
	res['direction'] = direction
	res['descent_direction'] = descent_direction
	return res
