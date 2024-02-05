from random import uniform

def simulate_darts(n: int) -> float:
    """
    Returns an approximation for pi using the Monte Carlo circle inscribed in a square method
    :param n: The sample size
    :return: An approximation for pi
    """
    n_in = 0
    for _ in range(n):
        x = uniform(-0.5, 0.5)
        y = uniform(-0.5, 0.5)
        if (x**2 + y**2)**0.5 <= 0.5:
            n_in += 1
    return 4 * n_in / n


