import numpy as np 
from statsmodels.stats.power import tt_ind_solve_power

class EffectSize:
    def __init__(self, 
                daily_ss_per_group, 
                baseline_conversion_rate, 
                max_lim_days, 
                power,
                confidence_level):
        self.daily_ss_per_group = daily_ss_per_group
        self.baseline_conversion_rate = baseline_conversion_rate
        self.max_lim_days = max_lim_days
        self.power = power
        self.confidence_level = confidence_level

    def compute_cumulative_ss(self) -> list:
        return np.cumsum([self.daily_ss_per_group] * self.max_lim_days)

    def compute_absolute_effect_size(self, l_ss_per_group: list) -> list:
        return [tt_ind_solve_power(nobs1 = ss,
                                power = self.power,
                                alpha = 1 - self.confidence_level,
                                alternative = 'two-sided') for ss in l_ss_per_group]

    def compute_relative_effect_size(self, l_absolute_effect_size: list) -> list:
        return [x / self.baseline_conversion_rate for x in l_absolute_effect_size]