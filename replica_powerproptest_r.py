import math
from scipy import stats


class Power:
    def __init__(self,
                 p1: float,
                 alpha: float,
                 beta: float):
        self.p1 = p1
        self.alpha = alpha
        self.beta = beta

    def compute_sample_size(self, delta: float) -> int:
        z_alpha = stats.norm.ppf(self.alpha / 2, loc=0, scale=1)
        z_beta = stats.norm.ppf(self.beta, loc=0, scale=1)
        
        p2 = self.p1 + delta
        p_avg = (self.p1 + p2) / 2
        
        left = z_alpha * math.sqrt(2 * p_avg * (1- p_avg))
        right = z_beta * math.sqrt(self.p1 * (1 - p1) + p2 * (1 - p2))
        numerator = (left + right) ** 2
        
        n = numerator / (delta ** 2)
        
        return int(math.ceil(n))

    def compute_delta(self, n: int) -> float:
        z_alpha = stats.norm.ppf(self.alpha / 2, loc=0, scale=1)
        z_beta = stats.norm.ppf(self.beta, loc=0, scale=1)
        z = (z_alpha + z_beta) ** 2
        
        p = 2 * self.p1 * (1 - self.p1) / n
        delta = math.sqrt(z * p)
        
        return round(delta, 3)
