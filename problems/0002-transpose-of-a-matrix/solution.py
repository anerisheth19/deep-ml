def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    res = []
    # for col in range(len(a[0])):
    #     new_row = []
    #     for row in a:
    #         new_row.append(row[col])
    #     res.append(new_row)

    import numpy as np
    res = np.transpose(a)

    return res

    # Your code here
    pass