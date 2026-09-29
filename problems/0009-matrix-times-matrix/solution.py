def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    if len(a[0]) != len(b):
        return -1

    c = []
    for r in range(len(a)): #row of a
        row = []
        for col in range(len(b[0])): #col of b
            total = 0
            for k in range(len(b)):
                total += a[r][k] * b[k][col] 
            
            row.append(total)
        c.append(row)         
    return c