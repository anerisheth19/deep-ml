import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # g(x) numerator
    g = 0
    for i in range(len(g_coeffs)):
        power = len(g_coeffs) - 1 - i
        g += g_coeffs[i] * x ** power
    
    # h(x) denominator
    h = 0
    for i in range(len(h_coeffs)):
        power = len(h_coeffs) - 1 - i
        h += h_coeffs[i] * x ** power
    
    # g'(x) numerator
    g_prime = 0
    for i in range(len(g_coeffs)):
        power = len(g_coeffs) - 1 - i
        if power > 0:
            g_prime += g_coeffs[i] * power * x ** (power-1)
    
    # h'(x) denominator
    h_prime = 0
    for i in range(len(h_coeffs)):
        power = len(h_coeffs) - 1 - i
        if power > 0:
            h_prime += h_coeffs[i] * power * x ** (power-1)
    
    return (g_prime * h - g * h_prime) / (h ** 2)
    # Your code here

    pass