import math
from scipy import stats


class Power:
    def __init__(self):
        pass

    @staticmethod
    def _compute_sample_size(p1: float, delta: float, alpha: float, beta: float) -> int:
        z_alpha = stats.norm.ppf(alpha / 2, loc=0, scale=1)
        z_beta = stats.norm.ppf(beta, loc=0, scale=1)
        
        p2 = p1 + delta
        p_avg = (p1 + p2) / 2
        
        left = z_alpha * math.sqrt(2 * p_avg * (1- p_avg))
        right = z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
        numerator = (left + right) ** 2
        
        n = numerator / (delta ** 2)
        
        return int(math.ceil(n))

    @staticmethod
    def _compute_delta(p1: float, n: int, alpha: float, beta: float) -> float:
        z_alpha = stats.norm.ppf(alpha / 2, loc=0, scale=1)
        z_beta = stats.norm.ppf(beta, loc=0, scale=1)
        z = (z_alpha + z_beta) ** 2
        
        p = 2 * p1 * (1 - p1) / n
        delta = math.sqrt(z * p)
        
        return round(delta, 3)
