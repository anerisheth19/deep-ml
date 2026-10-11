def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
		
	means = []
	if mode == "row":
		for row in matrix:
			mean = sum(row)/len(row)
			means.append(mean)
	
	if mode == "column":
		for col in range(len(matrix[0])):
			total = 0
			for row in range(len(matrix)):
				total += matrix[row][col]
			mean = total / len(matrix)
			means.append(mean)
	
	return means