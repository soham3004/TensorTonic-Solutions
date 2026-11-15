def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here'
    outp= x0
    for i in range(steps):
        grd = 2*a*outp + b
        outp = outp - lr*(grd)
    return outp
        